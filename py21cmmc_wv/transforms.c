#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <complex.h>

void morlet(int ndata, int n_nu, int n_eta, double conv_ext, double *data, double *nu, double *eta, complex double *out){
    // Discrete Morlet Wavelet transform, using Morlet basis from Goupillaud 1984 (Eq. 5, 6 - with b=2pi)

    //integer, intent(in)   :: nx, nt, nf
    //real(8), intent(in)   :: t(nt), tc(nt), f(nf)
    //real(8), intent(out)  :: rl_out(nx,nt,nf), im_out(nx,nt,nf)
    //real(8), intent(in)   :: realdata(nx, nt), imagdata(nx,nt)

    int ix, jc,jf, jt, thisn;
    double exponent, mag, extent, dt;

    dt = nu[1] - nu[0];

    double sqrt2 = sqrt(2.0);
    int index = 0;

    for (ix=0;ix<ndata;ix++){
        for (jc=0;jc<n_nu;jc++){
            for (jf=0; jf<n_eta;jf++){
            extent = 1/(eta[jf]*sqrt2);
            thisn = ceil(conv_ext*extent/dt);


                for (jt=fmax(0, jc-thisn); jt<fmin(jc+thisn, n_nu); jt++){
                    exponent = eta[jf]*(nu[jt] - nu[jc]);
                    out[index] += data[ix*n_nu + jt]*cexp(-exponent*(exponent/2 + 6.2831853071*I));
                }
                index++;
            }
        }
    }
}

void cmorlet(int ndata, int n_nu, int n_eta, double conv_ext, double complex *data, double *nu, double *eta, complex double *out){
    // Discrete Morlet Wavelet transform, using Morlet basis from Goupillaud 1984 (Eq. 5, 6 - with b=2pi)

    //integer, intent(in)   :: nx, nt, nf
    //real(8), intent(in)   :: t(nt), tc(nt), f(nf)
    //real(8), intent(out)  :: rl_out(nx,nt,nf), im_out(nx,nt,nf)
    //real(8), intent(in)   :: realdata(nx, nt), imagdata(nx,nt)

    int ix, jc,jf, jt, thisn;
    double exponent, mag, extent, dt;

    dt = nu[1] - nu[0];

    double sqrt2 = sqrt(2.0);
    int index = 0;

    for (ix=0;ix<ndata;ix++){
        for (jc=0;jc<n_nu;jc++){
            for (jf=0; jf<n_eta;jf++){
            extent = 1/(eta[jf]*sqrt2);
            thisn = ceil(conv_ext*extent/dt);


                for (jt=fmax(0, jc-thisn); jt<fmin(jc+thisn, n_nu); jt++){
                    exponent = eta[jf]*(nu[jt] - nu[jc]);
                    out[index] += data[ix*n_nu + jt]*cexp(-exponent*(exponent/2 + 6.2831853071*I));
                }
                index++;
            }
        }
    }
}