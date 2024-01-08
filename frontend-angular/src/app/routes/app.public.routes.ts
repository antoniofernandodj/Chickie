import { Routes } from '@angular/router';
import { LoginComponent } from '../pages/shared/login/login.component';
import { LogoutComponent } from '../pages/shared/logout/logout.component';
import { UserHomeComponent } from '../pages/public/home/home.component';
import { PedidoComponent } from '../pages/public/pedido/pedido.component';
import { SignupUserComponent } from '../pages/public/signup-user/signup-user.component';
import { LojaComponent } from '../pages/public/loja/loja.component';


export const publicRoutes: Routes = [

  { path: 'login',
    component: LoginComponent },

  { path: 'logout',
    component: LogoutComponent },

  { path: 'signup/user',
    component: SignupUserComponent },

  { path: 'user/home',
    component: UserHomeComponent },

  { path: 'pedidos/:pedidoID',
    component: PedidoComponent },

  { path: 'l/:lojaID',
    component: LojaComponent },

];
