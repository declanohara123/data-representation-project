from FilmsDao import filmsDao

film1 = {
    'ISBN': 1235,
    'title': 'Help',
    'director': 'Speilberg',
    'year': 2012,
}

film2 = {
    'ISBN': 1234,
    'title': 'aksb',
    'director': 'Tarantino',
    'year': 2015,
}

#returnvalue = filmsDao.create(film)
resultvalue = filmsDao.getAll()
print(resultvalue)

resultvalue = filmsDao.findById(film2['ISBN'])
print(resultvalue)
print("asca")

resultvalue = filmsDao.update(film2)
print(resultvalue)

resultvalue = filmsDao.findById(film2['ISBN'])
print(resultvalue)

resultvalue = filmsDao.delete(film2['ISBN'])
print(resultvalue)

resultvalue = filmsDao.getAll()
print(resultvalue)