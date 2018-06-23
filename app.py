from flask import Flask
from flask import jsonify
from flask import request
from flask_mysqldb import MySQL

import ast
from collections import Counter

app = Flask(__name__)

mysql = MySQL()
 
# MySQL configurations
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'resep-app'
app.config['MYSQL_HOST'] = 'localhost'

mysql.init_app(app)

# api to get bahan masakan
@app.route('/api/bahan', methods=['GET'])
def bahan():
    # optional parameter
    # search for search keyword (string)
    # contain for filter bahan, contain should be id bahan (array of string)
    # if no params api will return all bahan
    search = request.args.get('search')
    contain = request.args.get('contain')

    query = 'SELECT * FROM bahan'
    searchQuery = ''
    containQuery = ''

    if search is not None :
      searchQuery = 'LIKE '+ '"%' + search + '%"' + ''

    if contain is not None:
      contain = ast.literal_eval(contain)
      query = 'SELECT bahan.id_bahan, bahan.nama_bahan FROM `bahan` LEFT JOIN `masakan_bahan` ON bahan.id_bahan = masakan_bahan.id_bahan '
      listIdMasakan = cariListIdMasakanByBahan(contain)
      
      for idx, idMasakan in enumerate(listIdMasakan):
        filterQuery = '('
        if idx > 0: 
          filterQuery = 'OR '

        filterQuery = filterQuery + 'masakan_bahan.id_masakan = ' + str(idMasakan) + ' '

        if idx == (len(listIdMasakan) - 1):
          filterQuery = filterQuery + ')'

        containQuery = containQuery + filterQuery


    if (search is not None or contain is not None):
      query = query + ' WHERE '
      if search is not None and contain is not None:
        query = query + 'bahan.nama_bahan ' + searchQuery + ' AND ' + containQuery + ' GROUP BY bahan.id_bahan ORDER BY bahan.nama_bahan ASC'
      else :
        if search is not None:
          query = query + 'nama_bahan ' + searchQuery + 'ORDER BY nama_bahan ASC'
        
        if contain is not None:
          query = query + containQuery + ' GROUP BY bahan.id_bahan ORDER BY bahan.nama_bahan ASC'
    else:
      query = query + ' ORDER BY bahan.nama_bahan ASC'

    cur = mysql.connection.cursor()
    cur.execute(query)
    datas = cur.fetchall()
    bahan = []
    for data in datas:
      bahan.append({'id': data[0], 'nama': data[1]})

    return jsonify(data=bahan, error=False)

# api to get resep masakan
# if params bahan available api will return 1 resep else all resep
@app.route('/api/resep', methods=['GET'])
def resep():
  # optional parameter (bahan)
  # bahan should be bahan id (array of string)
  # if no params api will return all resep
  bahan = request.args.get('bahan')
  resepMemungkinkan = []

  query = 'SELECT * FROM masakan'
  if bahan is not None:
    bahan = ast.literal_eval(bahan)
    for item in bahan:
      masakanIdList = cariIdMasakanbyBahanId(item)
      for masakanId in masakanIdList:
        # if masakanId not in resepMemungkinkan:
        resepMemungkinkan.append(masakanId[0])

    resepMemungkinkan = Counter(resepMemungkinkan)
    query = query + ' WHERE '
    for idx, idMasakan in enumerate(resepMemungkinkan):
      query = query + 'id_masakan=' + str(idMasakan) + ' '
      if idx < (len(resepMemungkinkan) - 1): 
        query = query + 'OR '

  cur = mysql.connection.cursor()
  cur.execute(query)
  datas = cur.fetchall()
  resep = []

  for data in datas:
    resep.append({
      'id': data[0],
      'judul': data[1],
      'photo': data[2],
      'bahan_cocok': resepMemungkinkan[data[0]]
    })

  resep = sorted(resep, key=lambda item: item['id'], reverse=True)

  return jsonify(data=resep, error=False)

# api to get resep detail
@app.route('/api/resep/detail', methods=['GET'])
def resepDetail():
  # required parameteter
  # id masakan should be id resep masakan (string)
  idMasakan = request.args.get('id')

  if idMasakan is None:
    return jsonify(data=None, error=True)
  else:
    query = 'SELECT * FROM masakan WHERE id_masakan=' + str(idMasakan)
    cur = mysql.connection.cursor()
    cur.execute(query)
    data = cur.fetchone()
    resep = {
      'id': data[0],
      'judul': data[1],
      'photo': data[2],
      'resep': data[3],
      'bahan': cariBahanByIdMasakan(idMasakan)
    }

    return jsonify(data=resep, error=False)


# function to get all masakan that contain id bahan
def cariIdMasakanbyBahanId(id = None):
  if id is None:
    return None
  else:
    query = 'SELECT id_masakan from masakan_bahan where id_bahan = ' + str(id)
    cur = mysql.connection.cursor()
    cur.execute(query)
    data = cur.fetchall()
    return data

# function to get all masakan by id bahan
def cariListIdMasakanByBahan(bahan = None):
  if bahan is None:
    return None
  else :
    idList = []
    for item in bahan:
      idBahan = cariIdMasakanbyBahanId(item)
      if idBahan not in idList:
        idList.append(idBahan)
    return idList

# function to get all bahan masakan by id masakan
def cariBahanByIdMasakan(id = None):
  if id is None:
    return None
  else:
    query = 'SELECT masakan_bahan.id_bahan, bahan.nama_bahan, masakan_bahan.satuan FROM masakan_bahan LEFT JOIN bahan ON masakan_bahan.id_bahan = bahan.id_bahan WHERE masakan_bahan.id_masakan=' + id + ' ORDER BY bahan.nama_bahan ASC'
    cur = mysql.connection.cursor()
    cur.execute(query)
    datas = cur.fetchall()
    bahan = []
    for data in datas:
      bahan.append({'id': data[0], 'nama': data[1], 'jumlah': data[2]})
    return bahan
