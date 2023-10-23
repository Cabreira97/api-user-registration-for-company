import { sequelize } from '../database/conecta.js'

import { DataTypes } from 'sequelize'

export const Empresa = sequelize.define(
  'empresa',
  {
    id: {
      type: DataTypes.UUID,
      defaultValue: DataTypes.UUIDV4,
      primaryKey: true,
      autoIncrement: true
    },
    nome: {
      type: DataTypes.STRING(40),
      allowNull: false
    },
    cnpj: {
      type: DataTypes.STRING(14),
      allowNull: false
    },
    tamanho: {
      type: DataTypes.ENUM('pequena', 'media', 'grande'),
      allowNull: false
    },
    descricao: {
      type: DataTypes.TEXT,
      allowNull: false
    },
    razao_social: {
      type: DataTypes.STRING(100),
      allowNull: false
    }
  },
  {
    timestamps: false
  }
)
