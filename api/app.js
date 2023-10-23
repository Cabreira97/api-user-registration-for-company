import { sequelize } from './database/conecta.js'
import { Contratacao } from './models/Contratacao.js'
import { Empresa } from './models/Empresa.js'
import { Usuario } from './models/Usuario.js'
import router from './routes.js'

import express from 'express'
import fs from 'fs'
const app = express()
const port = 3000

app.use(express.json())
app.use(router)

app.get('/', (req, res) => {
  fs.readFile('index.html', 'utf8', (err, data) => {
    if (err) {
      return res.status(500).send('Erro ao ler o arquivo.')
    }

    res.send(data)
  })
})

async function conecta_db() {
  try {
    await sequelize.authenticate()
    console.log('Conectado com sucesso.')
    await Usuario.sync()
    console.log('Tabela Usuario criada com sucesso.📊')
    await Empresa.sync()
    console.log('Tabela Empresa criada com sucesso.📊')
    await Contratacao.sync()
    console.log('Tabela Contratacao criada com sucesso.📊')
  } catch (error) {
    console.error(
      'Não foi possível conectar ao banco de dados:📊',
      error
    )
  }
}
app.listen(port, () => {
  console.log(`🚀 API do Gupy esta rodadndo na porta 🚀 ${port}`)
})

conecta_db()
