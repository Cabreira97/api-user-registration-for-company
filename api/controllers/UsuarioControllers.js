import { Usuario } from '../models/Usuario.js'

export async function criarUsuario(req, res) {
  try {
    const novoUsuario = await Usuario.create(req.body)
    res.status(201).json(novoUsuario)
  } catch (error) {
    res.status(400).send(error)
  }
}

export async function listarUsuarios(req, res) {
  try {
    const usuarios = await Usuario.findAll()
    res.status(200).json(usuarios)
  } catch (error) {
    res.status(400).send(error)
  }
}

export async function atualizarUsuario(req, res) {
  try {
    const usuario = await Usuario.findByPk(req.params.id)
    if (!usuario) {
      return res
        .status(404)
        .json({ mensagem: 'Usuário não encontrado' })
    }
    await usuario.update(req.body)
    res.status(200).json(usuario)
  } catch (error) {
    res.status(400).send(error)
  }
}

export async function deletarUsuario(req, res) {
  try {
    const usuario = await Usuario.findByPk(req.params.id)
    if (!usuario) {
      return res
        .status(404)
        .json({ mensagem: 'Usuário não encontrado' })
    }
    await usuario.destroy()
    res.status(200).json({ mensagem: 'Usuário deletado com sucesso' })
  } catch (error) {
    res.status(400).send(error)
  }
}
