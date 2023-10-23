import { Contratacao } from '../models/Contratacao.js'

export async function criarContratacao(req, res) {
  try {
    const { regime, usuario_id, empresa_id } = req.body

    const novaContratacao = await Contratacao.create({
      regime,
      usuario_id,
      empresa_id
    })

    res.status(201).json(novaContratacao)
  } catch (error) {
    res.status(400).send(error)
  }
}

export async function listarContratacoes(req, res) {
  try {
    const contratacoes = await Contratacao.findAll()
    res.status(200).json(contratacoes)
  } catch (error) {
    res.status(400).send(error)
  }
}

export async function atualizarContratacao(req, res) {
  try {
    const contratacao = await Contratacao.findByPk(req.params.id)
    if (!contratacao) {
      return res
        .status(404)
        .json({ mensagem: 'Contratação não encontrada' })
    }
    await contratacao.update(req.body)
    res.status(200).json(contratacao)
  } catch (error) {
    res.status(400).send(error)
  }
}

export async function deletarContratacao(req, res) {
  try {
    const contratacao = await Contratacao.findByPk(req.params.id)
    if (!contratacao) {
      return res
        .status(404)
        .json({ mensagem: 'Contratação não encontrada' })
    }
    await contratacao.destroy()
    res
      .status(200)
      .json({ mensagem: 'Contratação deletada com sucesso' })
  } catch (error) {
    res.status(400).send(error)
  }
}
