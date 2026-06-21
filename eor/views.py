import json
from django.shortcuts import render


def articleone(request):
    return render(request, "article/articleone.html")

def articletwo(request):
    return render(request, "article/articletwo.html")

def articlethree(request):
    return render(request, "article/articlethree.html")

def articlefour(request):
    return render(request, "article/articlefour.html")

def home(request):
    return render(request, "home.html")



def mobility_ratio(request):

    result = None
    interpretation = None

    if request.method == "POST":

        krw = float(request.POST.get("krw"))
        kro = float(request.POST.get("kro"))
        muw = float(request.POST.get("muw"))
        muo = float(request.POST.get("muo"))

        # Mobility Ratio Formula
        result = (krw / muw) / (kro / muo)

        # Engineering interpretation
        if result < 1:
            interpretation = "Stable displacement (Good sweep efficiency) and More oil are produced"
        elif result == 1:
            interpretation = "Neutral displacement"
        else:
            interpretation = "Unstable displacement (Fingering likely), leading to Poor sweep efficiency and Oil pockets are bypassed"

    return render(request, "mobility_ratio.html", {
        "result": result,
        "interpretation": interpretation
    })



from django.shortcuts import render

def areal_sweep(request):

    result = None
    interpretation = None

    if request.method == "POST":

        As = float(request.POST.get("As"))
        At = float(request.POST.get("At"))

        result = (As / At) * 100

        if result < 30:
            interpretation = "Very Poor Areal Sweep . Water/gas breaks through very early . Large parts of reservoir are untouched . Injection process is inefficient and poorly controlled"
        elif result < 50:
            interpretation = "Poor sweep efficiency . high bypassed oil risk . Uneven displacement occur . Early breakthrough still occurs"
        elif result <= 70:
            interpretation = "Moderate sweep efficiency . About half to most of the reservoir area is contacted . Mixed stability (some fingering + some piston-like flow) . Water cut increases gradually"
        elif result <= 85:
            interpretation = "Good Sweep . Majority of reservoir area is contacted . Mostly stable flow . High oil recovery and delayed water breakthrough . Efficient waterflood or early EOR performance"
        elif result <= 95:
            interpretation = "Very Good Sweep . Almost entire reservoir area is contacted . Stable and controlled displacement . High cumulative oil production and Efficient recovery of remaining oil"
        else:
            interpretation = "Excellent / Near-Perfect Sweep . Almost full areal contact . Highly controlled displacement front . Maximum possible recovery from areal coverage perspective"

    return render(request, "areal_sweep.html", {
        "result": result,
        "interpretation": interpretation
    })



from django.shortcuts import render

def volumetric_sweep(request):

    result = None
    interpretation = None

    if request.method == "POST":

        EA = float(request.POST.get("EA"))
        ED = float(request.POST.get("ED"))
        EI = float(request.POST.get("EI"))

        result = EA * ED * EI

        if result < 0.2:
            interpretation = "Very Poor Volumetric Sweep . Most of the reservoir is untouched . Very large volume of oil completely bypassed . Reservoir is highly inefficiently swept — EOR is urgently needed"
        elif result < 0.4:
            interpretation = "Poor volumetric sweep (low reservoir contact) . Significant trapped oil in unswept layers . Basic waterflood performance but poor volumetric utilization"
        elif result <= 0.6:
            interpretation = "Good Volumetric Sweep . Most of reservoir volume is contacted . More uniform displacement . High recovery efficiency and only small isolated unswept zones remain . Efficient flood or early EOR performance"
        elif result <= 0.8:
            interpretation = "Very Good Sweep . Nearly all reservoir volume contacted . Stable, controlled displacement and good conformance control . Most recoverable oil is produced and only residual oil remains in tight pores"
        else:
            interpretation = "Excellent / Near-Complete Sweep . Almost entire reservoir volume is contacted . Highly uniform displacement . Maximum possible recovery from sweep perspective . Advanced EOR or highly optimized reservoir management"

    return render(request, "volumetric_sweep.html", {
        "result": result,
        "interpretation": interpretation
    })


from django.shortcuts import render

def breakthrough_time(request):

    result = None
    interpretation = None
    production_data = []

    if request.method == "POST":

        phi = float(request.POST.get("phi"))
        A = float(request.POST.get("A"))
        h = float(request.POST.get("h"))
        swi = float(request.POST.get("swi"))
        qw = float(request.POST.get("qw"))
        Bw = float(request.POST.get("Bw"))

        result = (phi * A * h * swi) / (qw * Bw)

        if result < 100:
            interpretation = "VERY EARLY BREAKTHROUGH . High permeability streaks . High mobility ratio (M >> 1) . Water appears almost immediately . Very poor sweep"
        elif result <= 300:
            interpretation = "EARLY BREAKTHROUGH . Moderate heterogeneity . Partial fingering . Water arrives early in production life . Oil production still significant initially"
        elif result <= 800:
            interpretation = "MODERATE BREAKTHROUGH . Normal sandstone reservoir . Moderate sweep efficiency . Balanced oil production phase . Water cut increases gradually"
        elif result <= 2000:
            interpretation = "DELAYED BREAKTHROUGH (GOOD RESERVOIR) . Good areal + vertical sweep . Controlled mobility ratio (M ≤ 1–1.5) . Long oil production period . Stable displacement front"
        else:
            interpretation = "VERY DELAYED BREAKTHROUGH (EXCELLENT) . Low mobility ratio (M < 1) . Uniform reservoir . Very long clean oil production . Efficient sweep across reservoir"

        # Simulated production decline curve
        base_rate = 1000

        for t in range(0, 10):
            oil_rate = base_rate * (0.88 ** t)

            production_data.append({
                "time": t,
                "oil_rate": oil_rate
            })

    return render(request, "breakthrough_time.html", {
        "result": result,
        "interpretation": interpretation,
        "production_data": production_data
    })


from django.shortcuts import render

def recovery_factor(request):

    result = None
    interpretation = None

    if request.method == "POST":

        Np = float(request.POST.get("Np"))
        N = float(request.POST.get("N"))

        result = (Np / N) * 100

        if result < 5:
            interpretation = "Very Early Reservoir Life . Production just started . Oil flow primarily controlled by natural pressure . More than 95% of OOIP still underground . Very early production stage . Reservoir contains nearly all original oil in place"
        elif result < 20:
            interpretation = "Primary Recovery Stage . Natural depletion is occurring . Oil production still relatively strong. Majority of oil remains trapped. Primary recovery operations. Primary recovery stage . Significant oil reserves remain available for secondary recovery"
        elif result <= 35:
            interpretation = "Average Waterflood Performance . Secondary recovery active . Water breakthrough may have occurred. Meaningful portion of OOIP recovered. Secondary recovery stage . Reservoir performance is typical of a mature waterflood."
        elif result <= 50:
            interpretation = "Good Waterflood Performance . Efficient pressure support . Good areal and vertical sweep . Controlled water production . Reservoir management is effective. Good recovery performance . Waterflood operations are effectively sweeping the reservoir"
        elif result <= 65:
            interpretation = "Excellent Recovery . Advanced waterflood or EOR . Efficient displacement . Strong reservoir management . Minimal bypassed movable oil . Majority of recoverable oil produced . Excellent recovery efficiency . Most movable oil has been produced"
        elif result <= 80:
            interpretation = "Advanced EOR Success . Enhanced displacement mechanisms active . Very little movable oil remains . Excellent sweep efficiency . Low residual oil saturation . Advanced recovery stage . EOR operations have significantly increased oil recovery"
        else:
            interpretation = "Exceptional Recovery . Rare achievement . Nearly complete recovery of movable oil . Most economically recoverable oil produced . Near theoretical recovery limits . Exceptional reservoir performance . Recovery approaches maximum practical limits"

    return render(request, "recovery_factor.html", {
        "result": result,
        "interpretation": interpretation
    })


from django.shortcuts import render

def mmp(request):

    result = None
    interpretation = None

    if request.method == "POST":

        T = float(request.POST.get("T"))
        API = float(request.POST.get("API"))

        # empirical constants (typical simplified values)
        a = 150
        b = 0.8
        c = 3.5

        result = a + (b * T) + (c * API)

        if result < 1500:
            interpretation = "Excellent Miscibility Conditions . Favorable temperature . The oil are light . Strong oil swelling and Reduced oil viscosity . Miscible flooding can be achieved easily . Excellent miscibility conditions . Reservoir pressure can readily achieve miscible displacement"
        elif result <= 2500:
            interpretation = "Good Miscibility Conditions . Typical light-to-medium crude oil . High recovery potential . Strong candidate for miscible gas flooding . Good miscibility conditions. Miscible gas injection is technically feasible"
        elif result <= 3500:
            interpretation = "Moderate Miscibility Conditions . Higher reservoir temperature . Miscibility possible but requires higher pressure maintenance . Moderate to good recovery improvements . Pressure management becomes important . Moderate miscibility requirements. Successful gas flooding depends on maintaining sufficient reservoir pressure"
        elif result <= 4500:
            interpretation = "Challenging Miscibility Conditions . Heavy crude or high-temperature reservoirs . Higher gas compression requirements . Increased operational costs . Miscible flooding may still work, but economics must be evaluated carefully . High miscibility pressure requirement. Additional compression and pressure support may be needed"
        elif result <= 6000:
            interpretation = "Difficult Miscibility Conditions . Heavy oils and a Very high reservoir temperatures . Miscibility difficult to maintain . Reduced economic attractiveness . Alternative EOR methods may be more suitable . Miscibility is difficult to achieve. Consider alternative EOR strategies or enhanced pressure maintenance"
        else:
            interpretation = "Very Difficult Miscibility Conditions . Heavy crude systems . Poor miscibility environment . Gas remains largely immiscible . Miscible gas injection is generally not preferred . Very high miscibility pressure requirement. Miscible gas flooding may be technically or economically impractical"

    return render(request, "mmp.html", {
        "result": result,
        "interpretation": interpretation
    })


from django.shortcuts import render

def fractional_flow(request):

    result = None
    interpretation = None

    if request.method == "POST":

        krw = float(request.POST.get("krw"))
        kro = float(request.POST.get("kro"))
        muw = float(request.POST.get("muw"))
        muo = float(request.POST.get("muo"))

        result = 1 / (1 + (kro * muw) / (krw * muo))

        if result < 0.2:
            interpretation = "Oil-Dominated Flow . Oil is the dominant flowing phase . Oil moves almost alone . Early stage of waterflood or near injection well . High oil cut (almost pure oil production) . Reservoir is still in “oil-only flow regime"
        elif result <= 0.4:
            interpretation = "Oil-Dominant Mixed Flow . Water starts becoming mobile and oil still dominates flow paths . Water starts forming connected paths. Oil production still high . Transition zone — early water encroachment"
        elif result <= 0.6:
            interpretation = "Balanced Flow Regime . Oil and water contribute equally to flow . Water begins pushing oil more effectively . Oil production starts declining . Active displacement zone — most efficient sweep happens here"
        elif result <= 0.8:
            interpretation = "Water-Dominant Flow . Water becomes the main flowing phase. Oil exists mainly as trapped or discontinuous phase . Oil production declining steadily . Waterflood is mature — breakthrough has occurred"
        elif result <= 0.95:
            interpretation = "Strong Water Flow . Water dominates almost completely . Oil is mostly residual or bypassed . Stable water channels . Very high water cut and low oil production . Late-stage waterflood / mature field"
        else:
            interpretation = "Almost Pure Water Flow . Oil flow is minimal . Reservoir is almost fully water-swept . Water is the only mobile phase . Mostly water production and oil becomes uneconomic . Field approaching abandonment or EOR required"

    return render(request, "fractional_flow.html", {
        "result": result,
        "interpretation": interpretation
    })


from django.shortcuts import render

def ooip(request):

    result = None

    interpretation = None

    if request.method == "POST":

        A = float(request.POST.get("A"))
        h = float(request.POST.get("h"))
        phi = float(request.POST.get("phi"))
        Sw = float(request.POST.get("Sw"))
        Bo = float(request.POST.get("Bo"))

        result = (7758 * A * h * phi * (1 - Sw)) / Bo

        if result < 1000000:
            interpretation = "Very Small Reservoir . Limited oil accumulation . Usually suited for small-scale development . Small hydrocarbon accumulation with limited reserves . Very small oil accumulation . Economic viability may depend on oil price and development cost"
        if result < 10000000:
            interpretation = "Small Reservoir . Commercially developable in some cases . Modest oil accumulation . Small independent field . Small reservoir with moderate development potential"
        if result < 100000000:
            interpretation = "Medium Reservoir . Typical standalone field . Long-term production possible . Commercial oil field with significant reserves . Medium-sized reservoir capable of supporting sustained production operations"
        if result < 500000000:
            interpretation = "Large Reservoir . Major field development . Multiple wells likely required. Long production life . Strong economic value . Large oil accumulation with substantial reserves . Large reservoir with strong development and recovery potential"
        if result < 1000000000:
            interpretation = "Very Large Reservoir . Strategic field asset . High investment opportunity . Multi-decade field life . Very significant hydrocarbon accumulation . Very large reservoir containing substantial recoverable resources"
        else:
            interpretation = "Giant Reservoir . World-class field . Extremely long production life . Massive economic impact . Giant oil field with exceptional resource potential . Giant reservoir . Resource volume is sufficient for major long-term field development"

    return render(request, "ooip.html", {
        "result": result,
        "interpretation": interpretation
    })


from django.shortcuts import render

def edbt(request):

    result = None
    interpretation = None

    if request.method == "POST":

        Sor = float(request.POST.get("Sor"))
        Sob = float(request.POST.get("Sob"))
        Swi = float(request.POST.get("Swi"))

        result = (Sor - Sob) / (Sor - Swi)

        if result < 0.2:
            interpretation = "Very Poor Displacement . Water/gas moves through reservoir with little oil displacement . Large amounts of oil remain in swept zones . Very low recovery before breakthrough . Strong bypassing at pore scale . Very poor microscopic displacement. Most oil remains trapped within swept pore spaces"
        elif result <= 0.4:
            interpretation = "Poor Displacement efficiency . Some oil are displaced . Moderate residual oil saturation . Limited recovery before breakthrough . Average waterflood performance . Poor displacement efficiency. Significant oil remains trapped in contacted zones"
        elif result <= 0.6:
            interpretation = "Moderate Displacement . Injected fluid displaces a reasonable amount of oil . Some trapped oil remains . Moderate residual oil saturation . Average recovery performance . Typical waterflood conditions . Moderate displacement efficiency. A substantial portion of movable oil has been displaced"
        elif result <= 0.8:
            interpretation = "God Displacement . Most movable oil displaced before breakthrough . Reduced capillary trapping . Most movable oil displaced before breakthrough . High recovery before breakthrough . Favorable mobility ratio . Good displacement efficiency. Most movable oil has been displaced from contacted pore spaces"
        elif result <= 0.95:
            interpretation = "Very Good Displacement . Very efficient oil displacement . Minimal trapped movable oil . Low residual oil saturation . Excellent recovery performance . Very good displacement efficiency. Optimized flood design and Strong mobility control . Only small amounts of movable oil remain in swept regions"
        else:
            interpretation = "Exceptional Displacement . Nearly complete displacement of movable oil . Maximum practical displacement efficiency . Often associated with miscible flooding and Advanced EOR performance . Exceptional displacement efficiency. Movable oil has been almost completely displaced from contacted pore spaces"

    return render(request, "edbt.html", {
        "result": result,
        "interpretation": interpretation
    })


from django.shortcuts import render
import math

def eabt(request):

    result = None
    interpretation = None

    if request.method == "POST":

        M = float(request.POST.get("M"))

        result = 0.55 + (0.032 / M) + (0.032 / math.exp(M)) - (0.005 * M)

        if result < 0.40:
            interpretation = "Very Poor Areal Sweep at Breakthrough . Severe viscous fingering . Highly unstable displacement front and Water/gas finds “short paths” . Most of the reservoir area is bypassed . Breakthrough happens too early . Very poor areal sweep. Large portions of the reservoir remain untouched at breakthrough"
        elif result <= 0.55:
            interpretation = "Poor Sweep . Significant fingering still present . Weak displacement front stability . Channeling through high-permeability zones . Moderate bypassed oil volume . Basic waterflood performance, but inefficient sweep pattern . Poor areal sweep efficiency at breakthrough. Significant unswept zones remain"
        elif result <= 0.70:
            interpretation = "Moderate Sweep . Reasonable area contacted before breakthrough . Some fingering present but not dominant . Mixed stable and unstable flow zones . Acceptable oil recovery efficiency . tandard field performance under normal mobility conditions . Moderate areal sweep. Reservoir is reasonably contacted before breakthrough"
        elif result <= 0.85:
            interpretation = "Good Sweep . Large portion of reservoir area contacted . Stable displacement front dominates . Controlled flow paths . Efficient reservoir drainage before breakthrough . Well-designed injection strategy or favorable mobility ratio (M ≤ 1–1.5) . Good areal sweep efficiency. Most of the reservoir area is contacted at breakthrough"
        elif result <= 0.95:
            interpretation = "Very Good Sweep . Nearly full areal coverage before breakthrough . Highly stable front propagation . High sweep efficiency and delayed breakthrough . Optimized pattern flood or polymer-assisted control . Very good areal sweep. Reservoir is efficiently contacted before breakthrough . "
        else:
            interpretation = "Excellent Sweep . Almost entire reservoir area contacted before breakthrough . Extremely stable displacement front . Maximum possible areal efficiency . Ideal flood conditions or very low mobility ratio (M < 1) . Excellent areal sweep efficiency. Nearly complete reservoir area is contacted at breakthrough"

    return render(request, "eabt.html", {
        "result": result,
        "interpretation": interpretation
    })



from django.shortcuts import render

def tbt(request):

    result = None
    interpretation = None
    selected_model = None

    if request.method == "POST":

        selected_model = request.POST.get("model")
        Iw = float(request.POST.get("Iw"))
        Qibt = float(request.POST.get("Qibt"))

        # Formula 1
        if selected_model == "pv":

            PV = float(request.POST.get("PV"))
            result = (PV * Qibt) / Iw

        # Formula 2
        elif selected_model == "geo":

            phi = float(request.POST.get("phi"))
            A = float(request.POST.get("A"))
            L = float(request.POST.get("L"))

            result = (phi * A * L * Qibt) / Iw

        # Interpretation
        if result < 100:
            interpretation = "Very Early Breakthrough . Water moves almost instantly to producer . Strong channeling / thief zones dominate . High permeability streaks control flow abd no uniform displacement front . Reservoir is highly inefficient or badly connected . Very early breakthrough. Severe channeling or high mobility ratio conditions dominate flow"
        elif result <= 300:
            interpretation = "Early Breakthrough . Partial reservoir volume is contacted . Mixed channeling + displacement . Basic waterflood performance but inefficient sweep . Some zones still unswept . Early breakthrough. Reservoir shows partial sweep with significant bypassed oil"
        elif result <= 800:
            interpretation = "Moderate Breakthrough Time . Reasonable portion of pore volume is swept before breakthrough . Stable flow in some regions . Transition between stable and unstable displacement . Standard waterflood performance . Moderate breakthrough time. Reservoir is being swept with average efficiency"
        elif result <= 2000:
            interpretation = "Good Breakthrough Delay . Large pore volume contacted before breakthrough . Stable displacement front . Mostly piston-like displacement . Limited fingering . Efficient reservoir management or good mobility control . Good breakthrough time. Efficient sweep and delayed water arrival"
        elif result <= 5000:
            interpretation = "Very Delayed Breakthrough . Almost full effective pore volume utilized before breakthrough . Excellent conformance control . Highly stable displacement front . Excellent reservoir performance or EOR-enhanced flood . Very delayed breakthrough, High reservoir sweep efficiency and strong displacement control"
        else:
            interpretation = "Excellent EOR performance Delayed breakthrough (efficient displacement)"

    return render(request, "tbt.html", {
        "result": result,
        "interpretation": interpretation,
        "selected_model": selected_model
    })


from django.shortcuts import render

def npbt(request):

    result = None
    interpretation = None

    if request.method == "POST":

        N = float(request.POST.get("N"))
        Eabt = float(request.POST.get("Eabt"))
        Edbt = float(request.POST.get("Edbt"))

        result = N * Eabt * Edbt

        if result < 10000:
            interpretation = "Low oil production at breakthrough (inefficient flood)"
        elif result <= 50000:
            interpretation = "Moderate oil production at breakthrough"
        else:
            interpretation = "High recovery efficiency at breakthrough"

    return render(request, "npbt.html", {
        "result": result,
        "interpretation": interpretation
    })


from django.shortcuts import render

def wibt(request):

    result = None
    interpretation = None
    selected_model = None

    if request.method == "POST":

        selected_model = request.POST.get("model")

        PV = float(request.POST.get("PV"))

        # Model 1: saturation-based
        if selected_model == "sat":

            Swf = float(request.POST.get("Swf"))
            Swi = float(request.POST.get("Swi"))

            result = PV * (Swf - Swi)

        # Model 2: injection-based
        elif selected_model == "inj":

            Qibt = float(request.POST.get("Qibt"))

            result = PV * Qibt

        # Interpretation
        # Interpretation


        if abs(result) < 0.10:
            interpretation = "Very Poor Sweep . danger . Water reached the production well after contacting only a small portion of the reservoir pore volume . Severe channeling, fingering, or thief-zone flow is likely occurring . Large volumes of oil remain bypassed and unswept . Very early breakthrough indicates poor conformance and inefficient flood performance . Consider mobility control methods such as polymer flooding, profile modification, or injection pattern optimization."
        elif abs(result) < 0.30:
            interpretation = "Poor Sweep . warning . Only a limited portion of reservoir pore volume was contacted before breakthrough . Partial sweep with noticeable fingering and heterogeneity effects . Significant oil remains trapped in unswept regions . Waterflood is functioning but sweep efficiency remains low . Evaluate injection rates, well spacing, and reservoir heterogeneity."
        elif abs(result) < 0.60:
            interpretation = "Moderate Sweep . info . A reasonable fraction of pore volume was contacted before breakthrough . Mixed stable and unstable displacement behavior . Moderate oil recovery achieved prior to breakthrough . Typical waterflood performance with acceptable reservoir utilization . Monitor water cut and optimize injection strategy to improve sweep."
        elif abs(result) < 0.80:
            interpretation = "Good Sweep . success . Most reservoir pore volume was contacted before breakthrough occurred . Stable displacement front with limited channeling . High oil recovery achieved before water breakthrough . Efficient sweep and good reservoir conformance . Continue current flood management practices and monitor breakthrough progression."
        else:
            interpretation = "Excellent Sweep . primary . A very large portion of the reservoir pore volume was contacted before breakthrough . Highly stable piston-like displacement behavior . Maximum practical oil recovery before breakthrough . Excellent reservoir management and flood efficiency. Reservoir demonstrates strong sweep efficiency and excellent conformance control."
            
    return render(request, "wibt.html", {
        "result": result,
        "interpretation": interpretation,
        "selected_model": selected_model
    })


from django.shortcuts import render

def qibt(request):

    result = None
    interpretation = None

    if request.method == "POST":

        model = request.POST.get("model")

        # Model 1: derivative-based
        if model == "dfw":

            dfw_dsw = float(request.POST.get("dfw_dsw"))

            result = 1 / dfw_dsw

        # Model 2: saturation difference
        elif model == "sat":

            Swf = float(request.POST.get("Swf"))
            Swi = float(request.POST.get("Swi"))

            result = Swf - Swi

        # Interpretation
        if result < 0.10:
            interpretation = "Very Poor Sweep . Water barely invades oil zone . Early breakthrough occurs . Very low pore volume utilization . Extremely inefficient displacement process . Very low water invasion before breakthrough. Severe channeling or poor sweep efficiency"
        elif result <= 0.20:
            interpretation = "Poor Sweep . Limited water penetration . Large oil zones untouched . Weak flood efficiency . Fingering present . Poor reservoir sweep. Limited pore volume contacted before breakthrough"
        elif result <= 0.30:
            interpretation = "Moderate Sweep . Some stable displacement zones . Reasonable pore invasion . Mixed stable + unstable flow . Normal waterflood performance . Moderate sweep efficiency. Significant portion of pore space contacted before breakthroug"
        elif result <= 0.40:
            interpretation = "Good Sweep . Strong water invasion before breakthrough . Most movable oil are displaced . Stable displacement front . Efficient waterflood . Good sweep efficiency. Large portion of reservoir pore space is utilized before breakthrough"
        else:
            interpretation = "Excellent Sweep . Very high water invasion before breakthrough . Highly efficient displacement . Near-piston-like behavior . Advanced EOR or very good reservoir . Excellent sweep efficiency. Reservoir shows highly effective pore-scale utilization before breakthrough"

    return render(request, "qibt.html", {
        "result": result,
        "interpretation": interpretation
    })


from django.shortcuts import render

def pv(request):

    result = None
    interpretation = None

    if request.method == "POST":

        phi = float(request.POST.get("phi"))
        A = float(request.POST.get("A"))
        L = float(request.POST.get("L"))

        result = (phi * A * L) / 5.615

        if result < 1000000:
            interpretation = "Very Small Reservoir Storage . Limited storage capacity . Small hydrocarbon system . Fast depletion possible . Small pore space volume . Very small pore volume. Reservoir has limited fluid storage capacity"
        elif result <= 10000000:
            interpretation = "Small Reservoir . Limited but commercial storage . Faster pressure response . Small-scale reservoir system . Small pore volume indicating limited reservoir storage capacity"
        elif result <= 100000000:
            interpretation = "Medium Reservoir . Normal field-scale storage . Balanced production behavior . Standard oil field reservoir size . Medium pore volume suitable for conventional field development"
        elif result <= 500000000:
            interpretation = "Large Reservoir . Strong storage capacity . Long production life . Major oil field scale . Large pore volume indicating strong hydrocarbon storage capacity"
        elif result <= 1000000000:
            interpretation = "Very Large Reservoir . Extensive reservoir system . High recovery potential . Strategic petroleum asset . Very large pore volume with significant reservoir storage capacity"
        else:
            interpretation = "Giant Reservoir . Massive hydrocarbon system . Multi-decade production potential . World-class reservoir . Giant pore volume representing an extremely large hydrocarbon storage system"

    return render(request, "pv.html", {
        "result": result,
        "interpretation": interpretation
    })


from django.shortcuts import render

def ns(request):

    result = None
    interpretation = None

    if request.method == "POST":

        model = request.POST.get("model")

        Bo = float(request.POST.get("Bo"))

        # Model 1: PV-based
        if model == "pv":

            PV = float(request.POST.get("PV"))
            Soi = float(request.POST.get("Soi"))

            result = (PV * Soi) / Bo

        # Model 2: volumetric
        elif model == "vol":

            A = float(request.POST.get("A"))
            h = float(request.POST.get("h"))
            phi = float(request.POST.get("phi"))
            Swi = float(request.POST.get("Swi"))

            result = (7758 * A * h * phi * (1 - Swi)) / Bo

        # Interpretation
        if result < 1000000:
            interpretation = "Very Small Reservoir . Small hydrocarbon accumulation . Marginal economics possible . Small oil accumulation with limited development potential . Very small oil accumulation. Commercial development may be constrained by economics"
        elif result <= 10000000:
            interpretation = "Small Reservoir . May support a limited development program . Modest oil accumulation . Small independent field . Commercially developable but relatively small reserve base . Small reservoir containing modest oil reserves"
        elif result <= 100000000:
            interpretation = "Medium Reservoir . Typical oil field size . Good development potential . Long-term production possible . Significant hydrocarbon accumulation . Medium-sized reservoir capable of supporting sustained production"
        elif result <= 500000000:
            interpretation = "Large Reservoir . Multiple production and injection wells . Strong long-term economic value . Large oil accumulation with substantial reserves . Large reservoir with strong production and recovery potential"
        elif result <= 1000000000:
            interpretation = "Very Large Reservoir . Long field life . Strategic asset . Major capital investment justified . Very significant oil accumulation . Very large reservoir containing substantial hydrocarbon resources"
        else:
            interpretation = "Giant Reservoir . World-class oil field and National-scale importance . Multi-decade development . Giant hydrocarbon accumulation . Giant reservoir with exceptional resource potential and long-term production capability"

    return render(request, "ns.html", {
        "result": result,
        "interpretation": interpretation
    })


# Graph part

import numpy as np
import matplotlib.pyplot as plt
import io
import base64
from django.shortcuts import render
import json

def relperm_plot(request):

    plot_url = None

    if request.method == "POST":

        sw_values = []
        kr_ratio_values = []

        # collect 15 values
        for i in range(1, 16):

            sw = request.POST.get(f"sw{i}")
            kr = request.POST.get(f"kr{i}")

            if sw and kr:
                sw_values.append(float(sw))
                kr_ratio_values.append(float(kr))

        # sort for proper plotting
        sorted_data = sorted(zip(sw_values, kr_ratio_values))
        sw_values, kr_ratio_values = zip(*sorted_data)

        # plotting
        plt.figure()
        plt.plot(sw_values, kr_ratio_values, marker='o', label="Kro/Krw vs Sw")

        plt.xlabel("Water Saturation (Sw)")
        plt.ylabel("Relative Permeability Ratio (Kro/Krw)")
        plt.title("Relative Permeability Curve")

        plt.grid(True)
        plt.legend()

        # auto scale
        plt.autoscale()

        # save image to memory
        buffer = io.BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)

        image_png = buffer.getvalue()
        buffer.close()

        plot_url = base64.b64encode(image_png).decode('utf-8')

        plt.close()

    return render(request, "relperm_plot.html", {
        "plot_url": plot_url
    })


from django.shortcuts import render

def fw_plot(request):

    plot_data = None

    if request.method == "POST":

        sw_values = []
        fw_values = []

        # collect 15 inputs
        for i in range(1, 16):

            sw = request.POST.get(f"sw{i}")
            fw = request.POST.get(f"fw{i}")

            if sw and fw:
                sw_values.append(float(sw))
                fw_values.append(float(fw))

        # sort for proper curve
        sorted_data = sorted(zip(sw_values, fw_values))
        sw_values, fw_values = zip(*sorted_data)

        # build chart data for frontend widget
        data = []
        for i in range(len(sw_values)):
            data.append({
                "Sw": sw_values[i],
                "Fw": fw_values[i]
            })

        plot_data = data

    return render(request, "fw_plot.html", {
        "plot_data": json.dumps(plot_data)
    })


from django.shortcuts import render

from django.shortcuts import render

def fw_dual_plot(request):

    plot_data = []

    if request.method == "POST":

        sw_values = []
        fw_values = []
        dfw_values = []

        for i in range(1, 16):

            sw = request.POST.get(f"sw{i}")
            fw = request.POST.get(f"fw{i}")
            dfw = request.POST.get(f"dfw{i}")

            if sw and fw and dfw:
                sw_values.append(float(sw))
                fw_values.append(float(fw))
                dfw_values.append(float(dfw))

        if len(sw_values) >= 2:

            combined = sorted(zip(sw_values, fw_values, dfw_values))
            sw_values, fw_values, dfw_values = zip(*combined)

            plot_data = [
                {
                    "Sw": float(sw_values[i]),
                    "Fw": float(fw_values[i]),
                    "dfw_dSw": float(dfw_values[i])
                }
                for i in range(len(sw_values))
            ]

    return render(request, "fw_dual.html", {
        "plot_data": json.dumps(plot_data)   # ✔ RAW PYTHON LIST (IMPORTANT)
    })



from django.shortcuts import render
import math

def slope(request):

    result = None
    interpretation = None

    if request.method == "POST":

        kro1 = float(request.POST.get("kro1"))
        krw1 = float(request.POST.get("krw1"))
        kro2 = float(request.POST.get("kro2"))
        krw2 = float(request.POST.get("krw2"))

        Sw1 = float(request.POST.get("Sw1"))
        Sw2 = float(request.POST.get("Sw2"))

        term1 = math.log(kro2 / krw2)
        term2 = math.log(kro1 / krw1)

        result = (term1 - term2) / (Sw2 - Sw1)

        if abs(result) > 1.0:
            interpretation = "Very Strong Instability . Rapid loss of oil mobility dominance . Strong water breakthrough tendency . Severe fingering expected . Early water channel formation . Poor flood stability . Very strong mobility contrast change. High risk of early water breakthrough and unstable displacement"
        elif abs(result) >= 0.5:
            interpretation = "Unstable Displacement . Noticeable mobility shift toward water . Partially unstable front . Moderate fingering development . Weak to moderate flood stability . Moderate instability in fractional flow behavior. Some fingering expected"
        elif abs(result) >= 0.2:
            interpretation = "Moderate Stability . Controlled displacement front . Balanced oil-water mobility transition . Transition zone stable in parts . Acceptable waterflood performance . Moderate fractional flow stability. Displacement is reasonably controlled"
        elif abs(result) >= 0.0:
            interpretation = "Stable Displacement . Smooth mobility transition . Oil and water interact in controlled way . Stable displacement front . Good waterflood performance . Stable fractional flow behavior. Good displacement efficiency expected"
        else:
            interpretation = "Highly Stable / Favorable Flood . Oil mobility remains strong longer . Water breakthrough delayed . Very stable or piston-like displacement . Excellent mobility control (often polymer or miscible conditions) . Highly stable fractional flow behavior. Excellent displacement efficiency and delayed breakthrough"

    return render(request, "slope.html", {
        "result": result,
        "interpretation": interpretation
    })



from django.shortcuts import render
from pint import UnitRegistry

ureg = UnitRegistry()

def unit_converter(request):

    result = None
    error = None

    if request.method == "POST":

        try:

            value = float(request.POST.get("value"))

            from_unit = request.POST.get("from_unit")
            to_unit = request.POST.get("to_unit")

            quantity = ureg.Quantity(value, from_unit)

            converted = quantity.to(to_unit)

            result = round(converted.magnitude, 6)

        except Exception as e:
            error = str(e)

    return render(request, "unit-converter.html", {
        "result": result,
        "error": error
    })


from django.shortcuts import render

def mobility(request):

    result = None
    interpretation = None

    if request.method == "POST":

        phase = request.POST.get("phase")

        kr = float(request.POST.get("kr"))
        mu = float(request.POST.get("mu"))

        result = kr / mu

        if result < 0.1:
            interpretation = "Low mobility"
        elif result < 1:
            interpretation = "Moderate mobility"
        else:
            interpretation = "High mobility"

    return render(request, "mobility.html", {
        "result": result,
        "interpretation": interpretation
    })


from django.shortcuts import render

def interpolation(request):

    result = None
    mode = None

    if request.method == "POST":

        mode = request.POST.get("mode")

        x1 = float(request.POST.get("x1"))
        y1 = float(request.POST.get("y1"))
        x2 = float(request.POST.get("x2"))
        y2 = float(request.POST.get("y2"))

        if mode == "solve_y":

            x = float(request.POST.get("x"))

            result = y1 + ((x - x1) * (y2 - y1)) / (x2 - x1)

        elif mode == "solve_x":

            y = float(request.POST.get("y"))

            result = x1 + ((y - y1) * (x2 - x1)) / (y2 - y1)

    return render(request, "interpolation.html", {
        "result": result,
        "mode": mode
    })


from django.shortcuts import render
import math

def dfw_dsw(request):

    result = None
    interpretation = None

    if request.method == "POST":

        muw = float(request.POST.get("muw"))
        muo = float(request.POST.get("muo"))
        a = float(request.POST.get("a"))
        b = float(request.POST.get("b"))
        Sw = float(request.POST.get("Sw"))

        viscosity_ratio = muw / muo

        numerator = -(
            viscosity_ratio *
            a *
            b *
            math.exp(b * Sw)
        )

        denominator = (
            1 +
            viscosity_ratio *
            a *
            math.exp(b * Sw)
        ) ** 2

        result = numerator / denominator

        if abs(result) > 5:
            interpretation = "Extremely Unstable Flood . Tiny saturation change causes sudden water dominance . Strong viscous fingering . Very early breakthrough . Poor mobility control . Extremely unstable displacement. Small changes in saturation cause rapid water breakthrough behavior"
        elif abs(result) > 2:
            interpretation = "Unstable Flow . Water quickly becomes dominant . Strong slope in fractional flow curve .Typical unfavorable waterflood . Unstable fractional flow behavior with strong sensitivity to saturation changes"
        elif abs(result) > 0.5:
            interpretation = "Transitional Flow . Balanced oil-water competition . Moderate sweep efficiency . Gradual change in fractional flow . Acceptable displacement stability . Moderate fractional flow sensitivity. Reservoir shows balanced displacement behavior"
        elif abs(result) > 0.1:
            interpretation = "Stable Flood . Smooth transition from oil to water flow . Controlled displacement front . Gradual fractional flow curve . Good waterflood performance . Stable fractional flow behavior with smooth displacement transition"
        else:
            interpretation = "Highly Stable / Near Piston Flow . Oil and water flow change slowly . Strong sweep efficiency . Flat fractional flow curve . Excellent mobility control (polymer or miscible conditions) . Highly stable displacement. Fractional flow is weakly sensitive to saturation changes"

    return render(
        request,
        "dfw_dsw.html",
        {
            "result": result,
            "interpretation": interpretation
        }
    )



from django.shortcuts import render

def mobility_ratio_breakthrough(request):

    result = None
    stage = "before"

    # Context fields the template references
    krw_swf = kro_swi = None
    krw_sw2 = kro_sw1 = None
    muo = muw = None

    if request.method == "POST":
        stage = request.POST.get("stage", "before")
        muo = float(request.POST.get("muo"))
        muw = float(request.POST.get("muw"))

        if stage == "before":
            krw_swf = float(request.POST.get("krw_swf"))
            kro_swi = float(request.POST.get("kro_swi"))
            result = (krw_swf / kro_swi) * (muo / muw)
        else:  # "after"
            krw_sw2 = float(request.POST.get("krw_sw2"))
            kro_sw1 = float(request.POST.get("kro_sw1"))
            result = (krw_sw2 / kro_sw1) * (muo / muw)

    return render(
        request,
        "mobility_ratio_breakthrough.html",
        {
            "result": result,
            "stage": stage,
            "krw_swf": krw_swf,
            "kro_swi": kro_swi,
            "krw_sw2": krw_sw2,
            "kro_sw1": kro_sw1,
            "muo": muo,
            "muw": muw,
        },
    )


# from django.shortcuts import render
# def mobility_ratio_breakthrough(request):

#     result_before = None
#     result_after = None

#     if request.method == "POST":

#         # BEFORE BREAKTHROUGH
#         krw_swf = float(request.POST.get("krw_swf"))
#         kro_swi = float(request.POST.get("kro_swi"))

#         # AFTER BREAKTHROUGH
#         krw_sw2 = float(request.POST.get("krw_sw2"))
#         kro_sw1 = float(request.POST.get("kro_sw1"))

#         muo = float(request.POST.get("muo"))
#         muw = float(request.POST.get("muw"))

#         result_before = (
#             (krw_swf / kro_swi)
#             * (muo / muw)
#         )

#         result_after = (
#             (krw_sw2 / kro_sw1)
#             * (muo / muw)
#         )

#     return render(
#         request,
#         "mobility_ratio_breakthrough.html",
#         {
#             "result_before": result_before,
#             "result_after": result_after
#         }
#     )