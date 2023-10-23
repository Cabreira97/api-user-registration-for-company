import { Sequelize } from 'sequelize'

export const sequelize = new Sequelize(
  'loja_brinquedos_thiago',
  'thiago',
  '123456',
  {
    host: 'localhost',
    dialect: 'mysql',
    port: 3306
  }
)
