import { sequelize } from '../database/conecta.js'
import { Empresa } from './Empresa.js'
import { Usuario } from './Usuario.js'

import { DataTypes } from 'sequelize'

export const Contratacao = sequelize.define(
  'contratacao',
  {
    id: {
      type: DataTypes.UUID,
      defaultValue: DataTypes.UUIDV4,
      primaryKey: true
    },
    regime: {
      type: DataTypes.ENUM('CLT', 'PJ'),
      allowNull: false
    }
  },
  {
    timestamps: false
  }
)

Usuario.hasMany(Contratacao, {
  foreignKey: 'usuario_id'
})
Empresa.hasMany(Contratacao, { foreignKey: 'empresa_id' })

Contratacao.belongsTo(Usuario, {
  foreignKey: 'usuario_id'
})
Contratacao.belongsTo(Empresa, { foreignKey: 'empresa_id' })
