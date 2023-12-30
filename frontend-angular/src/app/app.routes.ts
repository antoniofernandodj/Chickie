import { Routes } from '@angular/router';
import { LoginComponent } from './pages/login/login.component';
import { SignupComponent } from './pages/signup/signup.component';
import { PageNotFoundComponent } from './pages/page-not-found/page-not-found.component';
import { CompanyHomeComponent } from './pages/companyHome/companyHome.component';
import { CadastroCategoriaComponent } from './pages/cadastro-categoria/cadastro-categoria.component';
import { CadastroProdutoComponent } from './pages/cadastro-produto/cadastro-produto.component';
import { CategoriaComponent } from './pages/categoria/categoria.component';
import { LogoutComponent } from './pages/logout/logout.component';
import { ProdutoComponent } from './pages/produto/produto.component';
import { UserHomeComponent } from './pages/userHome/userHome.component';
import { PedidosComponent } from './pages/pedidos/pedidos.component';


export const routes: Routes = [
  { path: 'login', component: LoginComponent },
  { path: 'logout', component: LogoutComponent },
  { path: 'signup', component: SignupComponent },
  { path: 'empresa/home', component: CompanyHomeComponent },
  { path: 'user/home', component: UserHomeComponent },
  { path: 'empresa/categorias', component: CadastroCategoriaComponent },
  { path: 'empresa/categorias/:id', component: CategoriaComponent },
  { path: 'empresa/produtos/:id', component: ProdutoComponent },
  { path: 'empresa/produtos', component: CadastroProdutoComponent },
  { path: 'empresa/pedidos', component: PedidosComponent },
  { path: '**', component: PageNotFoundComponent },
];
