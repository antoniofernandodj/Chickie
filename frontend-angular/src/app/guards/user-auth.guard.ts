import { CanActivateFn } from '@angular/router';
import { AuthService } from '../services/auth.service';
import { inject } from '@angular/core';


const authService = inject(AuthService);

export const userAuthGuard: CanActivateFn = (route, state) => {
  const authService = inject(AuthService);
  const isActive = !!authService.currentUser();
  return isActive
};
