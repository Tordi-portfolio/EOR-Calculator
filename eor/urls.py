from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('mobility-ratio/', views.mobility_ratio, name='mobility_ratio'),
    path('areal-sweep/', views.areal_sweep, name='areal_sweep'),
    path('volumetric-sweep/', views.volumetric_sweep, name='volumetric_sweep'),
    path('breakthrough-time/', views.breakthrough_time, name='breakthrough_time'),
    path('recovery-factor/', views.recovery_factor, name='recovery_factor'),
    path('mmp/', views.mmp, name='mmp'),
    path('fractional-flow/', views.fractional_flow, name='fractional_flow'),
    path('ooip/', views.ooip, name='ooip'),
    path('edbt/', views.edbt, name='edbt'),
    path('eabt/', views.eabt, name='eabt'),
    path('tbt/', views.tbt, name='tbt'),
    path('npbt/', views.npbt, name='npbt'),
    path('wibt/', views.wibt, name='wibt'),
    path('qibt/', views.qibt, name='qibt'),
    path('pv/', views.pv, name='pv'),
    path('ns/', views.ns, name='ns'),
    path('relperm/', views.relperm_plot, name='relperm'),
    path('fw/', views.fw_plot, name='fw'),
    path('fw-dual/', views.fw_dual_plot, name='fw_dual'),
    path('slope/', views.slope, name='slope'),
    path('unit-converter/', views.unit_converter, name='unit_converter'),

    path('articleone/', views.articleone, name='articleone'),
    path('articletwo/', views.articletwo, name='articletwo'),
    path('articlethree/', views.articlethree, name='articlethree'),
    path('articlefour/', views.articlefour, name='articlefour'),
]
