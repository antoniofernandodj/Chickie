import { Routes } from '@angular/router';
import { CompanyHomeComponent } from '../pages/companyHome/companyHome.component';
import { CadastroCategoriaComponent } from '../pages/cadastro-categoria/cadastro-categoria.component';
import { CadastroProdutoComponent } from '../pages/cadastro-produto/cadastro-produto.component';
import { CategoriaComponent } from '../pages/categoria/categoria.component';
import { ProdutoComponent } from '../pages/produto/produto.component';
import { PedidosComponent } from '../pages/pedidos/pedidos.component';
import { StatusComponent } from '../pages/status/status.component';
import { companyAuthGuard } from '../guards/company-auth.guard';
import { LojaSettingsComponent } from '../pages/loja-settings/loja-settings.component';


export const lojaRoutes: Routes = [

  {
    path: 'loja/settings',
    component: LojaSettingsComponent,
    canActivate: [companyAuthGuard]
  },

  {
    path: 'loja/home',
    component: CompanyHomeComponent,
    canActivate: [companyAuthGuard]
  },

  {
    path: 'loja/categorias',
    component: CadastroCategoriaComponent,
    canActivate: [companyAuthGuard]
  },

  {
    path: 'loja/categorias/:id',
    component: CategoriaComponent,
    canActivate: [companyAuthGuard]
  },

  {
    path: 'loja/produtos/:id',
    component: ProdutoComponent,
    canActivate: [companyAuthGuard]
  },

  {
    path: 'loja/produtos',
    component: CadastroProdutoComponent,
    canActivate: [companyAuthGuard]
  },

  {
    path: 'loja/pedidos',
    component: PedidosComponent,
    canActivate: [companyAuthGuard]
  },

  {
    path: 'loja/status',
    component: StatusComponent,
    canActivate: [companyAuthGuard]
  },

];
