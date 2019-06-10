/*
 * brick_8FINALparam.java
 */

import com.comsol.model.*;
import com.comsol.model.util.*;
/** Model exported on Aug 14 2017, 10:42 by COMSOL 5.2.1.152. */
public class brick_8FINALparam {

  public static Model run() {
    Model model = ModelUtil.create("Model");

    model
         .modelPath("C:\\Users\\utilisateur\\Documents\\COURS\\4.IUT INFORMATIQUE A.S\\STAGE\\COMSOL\\NiceBricksModels");

    model.label("brick_8FINALparam.mph");

    model.comments("Untitled\n\n");

    model.param().set("t", "4 [mm]", "outer width");
    model.param().set("l", "1.33 [mm]", "bar length");
    model.param().set("ax", "12.5 [mm]", "brick height");
    model.param().set("ay", "12.5 [mm]", "brick width");
    model.param().set("w", "1 [mm]", "bar width");
    model.param().set("d", "3.1667 [mm]", "channel width");
    model.param().set("Ox", "-31.6", "originX (bottom left point)");
    model.param().set("Oy", "-5", "originY (bottom left point)");

    model.modelNode().create("comp1");

    model.geom().create("geom1", 2);

    model.mesh().create("mesh1", "geom1");

    model.geom("geom1").lengthUnit("mm");
    model.geom("geom1").create("r10", "Rectangle");
    model.geom("geom1").feature("r10").label("bar a");
    model.geom("geom1").feature("r10").set("size", new String[]{"l", "w"});
    model.geom("geom1").feature("r10").set("pos", new String[]{"(Ox+ax)-t-l", "Oy"});
    model.geom("geom1").create("r11", "Rectangle");
    model.geom("geom1").feature("r11").label("bar b");
    model.geom("geom1").feature("r11").set("size", new String[]{"l", "w"});
    model.geom("geom1").feature("r11").set("pos", new String[]{"Ox+t", "Oy+(w+d)"});
    model.geom("geom1").create("r19", "Rectangle");
    model.geom("geom1").feature("r19").label("bar c");
    model.geom("geom1").feature("r19").set("size", new String[]{"l", "w"});
    model.geom("geom1").feature("r19").set("pos", new String[]{"(Ox+ax)-t-l", "Oy+((2*w)+(2*d))"});
    model.geom("geom1").create("r14", "Rectangle");
    model.geom("geom1").feature("r14").label("top_boundary");
    model.geom("geom1").feature("r14").set("size", new String[]{"ax", "w"});
    model.geom("geom1").feature("r14").set("pos", new String[]{"Ox", "Oy+((3*w)+(3*d))"});
    model.geom("geom1").create("r15", "Rectangle");
    model.geom("geom1").feature("r15").label("right_boundary");
    model.geom("geom1").feature("r15").set("size", new String[]{"t", "ay+0.005"});
    model.geom("geom1").feature("r15").set("pos", new String[]{"(Ox+ax)-t", "Oy"});
    model.geom("geom1").create("r16", "Rectangle");
    model.geom("geom1").feature("r16").label("left_boundary");
    model.geom("geom1").feature("r16").set("size", new String[]{"t", "ay+0.005"});
    model.geom("geom1").feature("r16").set("pos", new String[]{"Ox", "Oy"});
    model.geom("geom1").create("uni1", "Union");
    model.geom("geom1").feature("uni1").selection("input")
         .set(new String[]{"r10", "r11", "r14", "r15", "r16", "r19"});
    model.geom("geom1").create("r17", "Rectangle");
    model.geom("geom1").feature("r17").label("air");
    model.geom("geom1").feature("r17").set("size", new String[]{"17.000003032146", "36.143958680246"});
    model.geom("geom1").feature("r17").set("pos", new String[]{"-33.600000882305", "-26.849998616782"});
    model.geom("geom1").create("r18", "Rectangle");
    model.geom("geom1").feature("r18").label("source");
    model.geom("geom1").feature("r18").set("size", new String[]{"17.000004888122", "1.1500021979122"});
    model.geom("geom1").feature("r18").set("pos", new String[]{"-33.600002205372", "-28.0"});
    model.geom("geom1").create("r22", "Rectangle");
    model.geom("geom1").feature("r22").label("left");
    model.geom("geom1").feature("r22").set("size", new String[]{"8.5661558864938", "35.999998465933"});
    model.geom("geom1").feature("r22").set("pos", new String[]{"-42.166156768799", "-28.000000867482"});
    model.geom("geom1").create("r23", "Rectangle");
    model.geom("geom1").feature("r23").label("right");
    model.geom("geom1").feature("r23").set("size", new String[]{"7.1535316060496", "35.999998789539"});
    model.geom("geom1").feature("r23").set("pos", new String[]{"-16.599996144624", "-28.000001191086"});
    model.geom("geom1").create("r24", "Rectangle");
    model.geom("geom1").feature("r24").label("bottom");
    model.geom("geom1").feature("r24").set("size", new String[]{"32.719692717863", "7.5"});
    model.geom("geom1").feature("r24").set("pos", new String[]{"-42.166156940367", "-35.513125429547"});
    model.geom("geom1").create("r25", "Rectangle");
    model.geom("geom1").feature("r25").label("top");
    model.geom("geom1").feature("r25").set("size", new String[]{"32.71969132933", "7.4552136725431"});
    model.geom("geom1").feature("r25").set("pos", new String[]{"-42.166156940367", "8"});
    model.geom("geom1").create("dif1", "Difference");
    model.geom("geom1").feature("dif1").selection("input2").set(new String[]{"uni1"});
    model.geom("geom1").feature("dif1").selection("input").set(new String[]{"r17"});
    model.geom("geom1").create("sca1", "Scale");
    model.geom("geom1").feature("sca1").set("type", "anisotropic");
    model.geom("geom1").feature("sca1").set("factor", new String[]{"1", "0.9641998076462"});
    model.geom("geom1").feature("sca1").set("pos", new String[]{"-25.1", "-26.85"});
    model.geom("geom1").feature("sca1").selection("input").set(new String[]{"dif1"});
    model.geom("geom1").run();

    model.material().create("mat4", "Common", "comp1");
    model.material().create("mat5", "Common", "comp1");
    model.material("mat4").selection().set(new int[]{5});
    model.material("mat4").propertyGroup("def").func().create("eta", "Piecewise");
    model.material("mat4").propertyGroup("def").func().create("Cp", "Piecewise");
    model.material("mat4").propertyGroup("def").func().create("rho", "Analytic");
    model.material("mat4").propertyGroup("def").func().create("k", "Piecewise");
    model.material("mat4").propertyGroup("def").func().create("cs", "Analytic");
    model.material("mat4").propertyGroup().create("RefractiveIndex", "Refractive index");
    model.material("mat5").selection().set(new int[]{4});
    model.material("mat5").propertyGroup().create("Enu", "Young's modulus and Poisson's ratio");

    model.coordSystem().create("pml1", "geom1", "PML");
    model.coordSystem("pml1").selection().set(new int[]{1, 2, 3, 6});

    model.physics().create("acpr", "PressureAcoustics", "geom1");
    model.physics("acpr").selection().set(new int[]{5});
    model.physics("acpr").create("mls1", "FrequencyMonopoleLineSource", 0);
    model.physics("acpr").create("pwr1", "PlaneWaveRadiation", 1);
    model.physics("acpr").feature("pwr1").selection().set(new int[]{12});
    model.physics("acpr").feature("pwr1").create("ipf1", "IncidentPressureField", 1);

    model.mesh("mesh1").create("ftri1", "FreeTri");
    model.mesh("mesh1").feature("ftri1").selection().geom("geom1", 2);
    model.mesh("mesh1").feature("ftri1").selection().set(new int[]{5});

    model.view("view1").axis().set("abstractviewrratio", "0.11236107349395752");
    model.view("view1").axis().set("abstractviewlratio", "-0.11680889129638672");
    model.view("view1").axis().set("abstractviewxscale", "0.047275789082050323");
    model.view("view1").axis().set("abstractviewbratio", "0.340532511472702");
    model.view("view1").axis().set("xmax", "-14.6202974319458");
    model.view("view1").axis().set("xmin", "-35.65806579589844");
    model.view("view1").axis().set("abstractviewyscale", "0.04727579280734062");
    model.view("view1").axis().set("ymax", "9.149118423461914");
    model.view("view1").axis().set("ymin", "-14.982440948486328");
    model.view("view1").axis().set("abstractviewtratio", "0.028303740546107292");

    model.material("mat4").label("Air");
    model.material("mat4").set("family", "air");
    model.material("mat4").propertyGroup("def").func("eta")
         .set("pieces", new String[][]{{"200.0", "1600.0", "-8.38278E-7+8.35717342E-8*T^1-7.69429583E-11*T^2+4.6437266E-14*T^3-1.06585607E-17*T^4"}});
    model.material("mat4").propertyGroup("def").func("eta").set("arg", "T");
    model.material("mat4").propertyGroup("def").func("Cp")
         .set("pieces", new String[][]{{"200.0", "1600.0", "1047.63657-0.372589265*T^1+9.45304214E-4*T^2-6.02409443E-7*T^3+1.2858961E-10*T^4"}});
    model.material("mat4").propertyGroup("def").func("Cp").set("arg", "T");
    model.material("mat4").propertyGroup("def").func("rho").set("args", new String[]{"pA", "T"});
    model.material("mat4").propertyGroup("def").func("rho").set("expr", "pA*0.02897/8.314/T");
    model.material("mat4").propertyGroup("def").func("rho").set("dermethod", "manual");
    model.material("mat4").propertyGroup("def").func("rho")
         .set("plotargs", new String[][]{{"pA", "0", "1"}, {"T", "0", "1"}});
    model.material("mat4").propertyGroup("def").func("rho")
         .set("argders", new String[][]{{"pA", "d(pA*0.02897/8.314/T,pA)"}, {"T", "d(pA*0.02897/8.314/T,T)"}});
    model.material("mat4").propertyGroup("def").func("k")
         .set("pieces", new String[][]{{"200.0", "1600.0", "-0.00227583562+1.15480022E-4*T^1-7.90252856E-8*T^2+4.11702505E-11*T^3-7.43864331E-15*T^4"}});
    model.material("mat4").propertyGroup("def").func("k").set("arg", "T");
    model.material("mat4").propertyGroup("def").func("cs").set("args", new String[]{"T"});
    model.material("mat4").propertyGroup("def").func("cs").set("expr", "sqrt(1.4*287*T)");
    model.material("mat4").propertyGroup("def").func("cs").set("dermethod", "manual");
    model.material("mat4").propertyGroup("def").func("cs").set("plotargs", new String[][]{{"T", "0", "1"}});
    model.material("mat4").propertyGroup("def").func("cs")
         .set("argders", new String[][]{{"T", "d(sqrt(1.4*287*T),T)"}});
    model.material("mat4").propertyGroup("def")
         .set("relpermeability", new String[]{"1", "0", "0", "0", "1", "0", "0", "0", "1"});
    model.material("mat4").propertyGroup("def")
         .set("relpermittivity", new String[]{"1", "0", "0", "0", "1", "0", "0", "0", "1"});
    model.material("mat4").propertyGroup("def").set("dynamicviscosity", "eta(T[1/K])[Pa*s]");
    model.material("mat4").propertyGroup("def").set("ratioofspecificheat", "1.4");
    model.material("mat4").propertyGroup("def")
         .set("electricconductivity", new String[]{"0[S/m]", "0", "0", "0", "0[S/m]", "0", "0", "0", "0[S/m]"});
    model.material("mat4").propertyGroup("def").set("heatcapacity", "Cp(T[1/K])[J/(kg*K)]");
    model.material("mat4").propertyGroup("def").set("density", "rho(pA[1/Pa],T[1/K])[kg/m^3]");
    model.material("mat4").propertyGroup("def")
         .set("thermalconductivity", new String[]{"k(T[1/K])[W/(m*K)]", "0", "0", "0", "k(T[1/K])[W/(m*K)]", "0", "0", "0", "k(T[1/K])[W/(m*K)]"});
    model.material("mat4").propertyGroup("def").set("soundspeed", "cs(T[1/K])[m/s]");
    model.material("mat4").propertyGroup("def").addInput("temperature");
    model.material("mat4").propertyGroup("def").addInput("pressure");
    model.material("mat4").propertyGroup("RefractiveIndex").set("n", "");
    model.material("mat4").propertyGroup("RefractiveIndex").set("ki", "");
    model.material("mat4").propertyGroup("RefractiveIndex")
         .set("n", new String[]{"1", "0", "0", "0", "1", "0", "0", "0", "1"});
    model.material("mat4").propertyGroup("RefractiveIndex")
         .set("ki", new String[]{"0", "0", "0", "0", "0", "0", "0", "0", "0"});
    model.material("mat5").label("Acrylic plastic");
    model.material("mat5").set("ambient", "custom");
    model.material("mat5").set("specular", "custom");
    model.material("mat5").set("noise", "on");
    model.material("mat5").set("family", "custom");
    model.material("mat5").set("diffuse", "custom");
    model.material("mat5").set("noisefreq", "1");
    model.material("mat5")
         .set("customambient", new String[]{"0.39215686274509803", "0.7843137254901961", "0.39215686274509803"});
    model.material("mat5").set("lighting", "phong");
    model.material("mat5").set("shininess", "1000");
    model.material("mat5")
         .set("customspecular", new String[]{"0.9803921568627451", "0.9803921568627451", "0.9803921568627451"});
    model.material("mat5")
         .set("customdiffuse", new String[]{"0.39215686274509803", "0.7843137254901961", "0.39215686274509803"});
    model.material("mat5").propertyGroup("def")
         .set("thermalexpansioncoefficient", new String[]{"7.0e-5[1/K]", "0", "0", "0", "7.0e-5[1/K]", "0", "0", "0", "7.0e-5[1/K]"});
    model.material("mat5").propertyGroup("def").set("heatcapacity", "1470[J/(kg*K)]");
    model.material("mat5").propertyGroup("def").set("density", "1190[kg/m^3]");
    model.material("mat5").propertyGroup("def")
         .set("thermalconductivity", new String[]{"0.18[W/(m*K)]", "0", "0", "0", "0.18[W/(m*K)]", "0", "0", "0", "0.18[W/(m*K)]"});
    model.material("mat5").propertyGroup("Enu").set("youngsmodulus", "3.2e9[Pa]");
    model.material("mat5").propertyGroup("Enu").set("poissonsratio", "0.35");

    model.physics("acpr").feature("pwr1").feature("ipf1").set("pamp", "1");
    model.physics("acpr").feature("pwr1").feature("ipf1").set("c", "365");

    model.mesh("mesh1").feature("size").set("hauto", 2);
    model.mesh("mesh1").run();

    model.study().create("std1");
    model.study("std1").create("freq", "Frequency");

    model.sol().create("sol1");
    model.sol("sol1").study("std1");
    model.sol("sol1").attach("std1");
    model.sol("sol1").create("st1", "StudyStep");
    model.sol("sol1").create("v1", "Variables");
    model.sol("sol1").create("s1", "Stationary");
    model.sol("sol1").feature("s1").create("p1", "Parametric");
    model.sol("sol1").feature("s1").create("fc1", "FullyCoupled");
    model.sol("sol1").feature("s1").feature().remove("fcDef");

    model.result().create("pg1", "PlotGroup2D");
    model.result().create("pg2", "PlotGroup2D");
    model.result("pg1").create("surf1", "Surface");
    model.result("pg2").create("surf1", "Surface");
    model.result().export().create("anim1", "Animation");

    model.study("std1").feature("freq").set("punit", "kHz");
    model.study("std1").feature("freq").set("plist", "3.43");

    model.sol("sol1").attach("std1");
    model.sol("sol1").feature("v1").set("clist", new String[]{"3.43[kHz]"});
    model.sol("sol1").feature("v1").set("cname", new String[]{"freq"});
    model.sol("sol1").feature("v1").set("clistctrl", new String[]{"p1"});
    model.sol("sol1").feature("s1").feature("aDef").set("complexfun", true);
    model.sol("sol1").feature("s1").feature("p1").set("punit", new String[]{"kHz"});
    model.sol("sol1").feature("s1").feature("p1").set("plistarr", new String[]{"3.43"});
    model.sol("sol1").feature("s1").feature("p1").set("pname", new String[]{"freq"});
    model.sol("sol1").feature("s1").feature("p1").set("preusesol", "auto");
    model.sol("sol1").feature("s1").feature("p1").set("pcontinuationmode", "no");
    model.sol("sol1").runAll();

    model.result("pg1").label("Acoustic Pressure (acpr)");
    model.result("pg1").set("edgecolor", "custom");
    model.result("pg1").feature("surf1").set("expr", "abs(acpr.p_t)");
    model.result("pg1").feature("surf1").set("descr", "abs(acpr.p_t)");
    model.result("pg1").feature("surf1").set("colortable", "HeatCameraLight");
    model.result("pg1").feature("surf1").set("resolution", "normal");
    model.result("pg2").label("Sound Pressure Level (acpr)");
    model.result("pg2").feature("surf1").set("unit", "dB");
    model.result("pg2").feature("surf1").set("expr", "acpr.Lp");
    model.result("pg2").feature("surf1").set("rangecolormin", "70");
    model.result("pg2").feature("surf1").set("descr", "Sound pressure level");
    model.result("pg2").feature("surf1").set("rangecoloractive", "on");
    model.result("pg2").feature("surf1").set("rangecolormax", "106.477482405148");
    model.result("pg2").feature("surf1").set("resolution", "normal");
    model.result().export("anim1").set("sweeptype", "dde");
    model.result().export("anim1").set("shownparameter", "0");
    model.result().export("anim1").set("repeat", true);
    model.result().export("anim1").set("target", "player");
    model.result().export("anim1").set("title", "on");
    model.result().export("anim1").set("legend", "on");
    model.result().export("anim1").set("logo", "on");
    model.result().export("anim1").set("options", "off");
    model.result().export("anim1").set("fontsize", "9");
    model.result().export("anim1").set("customcolor", new double[]{1, 1, 1});
    model.result().export("anim1").set("background", "color");
    model.result().export("anim1").set("axisorientation", "on");
    model.result().export("anim1").set("grid", "on");
    model.result().export("anim1").set("axes", "on");
    model.result().export("anim1").set("showgrid", "on");

    model.label("brick_3FINALparam.mph");

    model.result("pg1").run();

    model.mesh("mesh1").run();

    model.geom("geom1").run("r16");
    model.geom("geom1").feature().move("r16", 3);
    model.geom("geom1").run("r16");
    model.geom("geom1").feature("r16").set("size", new String[]{"t", "ay"});
    model.geom("geom1").feature("r14").set("pos", new String[]{"Ox", "Oy+ay"});
    model.geom("geom1").run("r14");
    model.geom("geom1").feature("r15").set("size", new String[]{"t", "ay"});
    model.geom("geom1").run("r15");
    model.geom("geom1").runPre("fin");

    model.mesh("mesh1").run();

    return model;
  }

  public static void main(String[] args) {
    run();
  }

}
