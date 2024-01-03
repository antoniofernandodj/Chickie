import { CanActivateFn } from '@angular/router';
import { AuthService } from '../services/auth.service';
import { inject } from '@angular/core';


export const companyAuthGuard: CanActivateFn = (route, state) => {
  const authService = inject(AuthService);
  const isActive = !!authService.currentCompany();
  return isActive
};
