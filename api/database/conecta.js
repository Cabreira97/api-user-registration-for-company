import { Sequelize } from 'sequelize'

export const sequelize = new Sequelize(
  'nome do seu banco',
  'usuário',
  'senha',
  {
    host: 'localhost',
    dialect: 'mysql',
    port: 3306
  }
)
