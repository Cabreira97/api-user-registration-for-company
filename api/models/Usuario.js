import { sequelize } from '../database/conecta.js'

import { DataTypes } from 'sequelize'

export const Usuario = sequelize.define(
  'usuario',
  {
    id: {
      type: DataTypes.UUID,
      defaultValue: DataTypes.UUIDV4,
      primaryKey: true
    },
    nome: {
      type: DataTypes.STRING(40),
      allowNull: false
    },
    nivel: {
      type: DataTypes.ENUM('junior', 'pleno', 'senior'), // Adicionando as opções
      allowNull: false
    },
    anos_experiencia: {
      type: DataTypes.INTEGER,
      allowNull: false
    },
    salario: {
      type: DataTypes.FLOAT,
      allowNull: false
    },
    area: {
      type: DataTypes.STRING(40),
      allowNull: false
    },
    linguagem: {
      type: DataTypes.STRING(40),
      allowNull: false
    },
    cargo_pretendido: {
      type: DataTypes.STRING(40),
      allowNull: false
    }
  },
  {
    timestamps: false
  }
)
