import { Empresa } from '../models/Empresa.js'

export async function criarEmpresa(req, res) {
  try {
    const novaEmpresa = await Empresa.create(req.body)
    res.status(201).json(novaEmpresa)
  } catch (error) {
    res.status(400).send(error)
  }
}

export async function listarEmpresas(req, res) {
  try {
    const empresas = await Empresa.findAll()
    res.status(200).json(empresas)
  } catch (error) {
    res.status(400).send(error)
  }
}

export async function atualizarEmpresa(req, res) {
  try {
    const empresa = await Empresa.findByPk(req.params.id)
    if (!empresa) {
      return res
        .status(404)
        .json({ mensagem: 'Empresa não encontrada' })
    }
    await empresa.update(req.body)
    res.status(200).json(empresa)
  } catch (error) {
    res.status(400).send(error)
  }
}

export async function deletarEmpresa(req, res) {
  try {
    const empresa = await Empresa.findByPk(req.params.id)
    if (!empresa) {
      return res
        .status(404)
        .json({ mensagem: 'Empresa não encontrada' })
    }
    await empresa.destroy()
    res.status(200).json({ mensagem: 'Empresa deletada com sucesso' })
  } catch (error) {
    res.status(400).send(error)
  }
}
