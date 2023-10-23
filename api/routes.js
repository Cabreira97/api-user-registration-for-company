import {
  atualizarContratacao,
  criarContratacao,
  deletarContratacao,
  listarContratacoes
} from './controllers/ContratacaoControllers.js'
import {
  atualizarEmpresa,
  criarEmpresa,
  deletarEmpresa,
  listarEmpresas
} from './controllers/EmpresaControllers.js'
import {
  atualizarUsuario,
  criarUsuario,
  deletarUsuario,
  listarUsuarios
} from './controllers/UsuarioControllers.js'

import { Router } from 'express'

const router = Router()

// Rotas para UsuarioDesenvolvedor
router.post('/usuarios', criarUsuario)
router.get('/usuarios', listarUsuarios)
router.put('/usuarios/:id', atualizarUsuario)
router.delete('/usuarios/:id', deletarUsuario)

// Rotas para Empresa
router.post('/empresas', criarEmpresa)
router.get('/empresas', listarEmpresas)
router.put('/empresas/:id', atualizarEmpresa)
router.delete('/empresas/:id', deletarEmpresa)

// Rotas para Contratacao
router.post('/contratacoes', criarContratacao)
router.get('/contratacoes', listarContratacoes)
router.put('/contratacoes/:id', atualizarContratacao)
router.delete('/contratacoes/:id', deletarContratacao)

export default router
