import { Routes } from '@angular/router';
import { LoginComponent } from './pages/login/login.component';
import { PageNotFoundComponent } from './pages/page-not-found/page-not-found.component';
import { CompanyHomeComponent } from './pages/companyHome/companyHome.component';
import { CadastroCategoriaComponent } from './pages/cadastro-categoria/cadastro-categoria.component';
import { CadastroProdutoComponent } from './pages/cadastro-produto/cadastro-produto.component';
import { CategoriaComponent } from './pages/categoria/categoria.component';
import { LogoutComponent } from './pages/logout/logout.component';
import { ProdutoComponent } from './pages/produto/produto.component';
import { UserHomeComponent } from './pages/userHome/userHome.component';
import { PedidosComponent } from './pages/pedidos/pedidos.component';
import { PedidoComponent } from './pages/pedido/pedido.component';
import { StatusComponent } from './pages/status/status.component';
import { SignupEmpresaComponent } from './pages/signup-empresa/signup-empresa.component';
import { SignupUserComponent } from './pages/signup-user/signup-user.component';
import { LojaComponent } from './pages/loja/loja.component';


export const routes: Routes = [
  { path: 'login', component: LoginComponent },
  { path: 'logout', component: LogoutComponent },
  { path: 'loja/home', component: CompanyHomeComponent },
  { path: 'user/home', component: UserHomeComponent },
  { path: 'loja/categorias', component: CadastroCategoriaComponent },
  { path: 'loja/categorias/:id', component: CategoriaComponent },
  { path: 'loja/produtos/:id', component: ProdutoComponent },
  { path: 'l/:lojaID', component: LojaComponent },
  { path: 'loja/produtos', component: CadastroProdutoComponent },
  { path: 'loja/pedidos', component: PedidosComponent },
  { path: 'loja/status', component: StatusComponent },
  { path: 'pedidos/:pedidoID', component: PedidoComponent },
  { path: 'signup/empresa', component: SignupEmpresaComponent },
  { path: 'signup/user', component: SignupUserComponent },
  { path: '**', component: PageNotFoundComponent },
];
