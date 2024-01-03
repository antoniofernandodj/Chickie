import { Routes } from '@angular/router';
import { LoginComponent } from '../pages/login/login.component';
import { LogoutComponent } from '../pages/logout/logout.component';
import { UserHomeComponent } from '../pages/userHome/userHome.component';
import { PedidoComponent } from '../pages/pedido/pedido.component';
import { SignupEmpresaComponent } from '../pages/signup-empresa/signup-empresa.component';
import { SignupUserComponent } from '../pages/signup-user/signup-user.component';
import { LojaComponent } from '../pages/loja/loja.component';


export const publicRoutes: Routes = [

  {
    path: 'login',
    component: LoginComponent
  },

  {
    path: 'logout',
    component: LogoutComponent
  },

  {
    path: 'signup/empresa',
    component: SignupEmpresaComponent
  },

  {
    path: 'signup/user',
    component: SignupUserComponent
  },

  {
    path: 'user/home',
    component: UserHomeComponent
  },

  {
    path: 'pedidos/:pedidoID',
    component: PedidoComponent
  },

  {
    path: 'l/:lojaID',
    component: LojaComponent
  },

];
