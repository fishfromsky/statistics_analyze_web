execute
CPX_PARAM
{
cplex.TiLim = 30;
cplex.epgap =  0.02; 						// gap:{{cplex_epgap}}

}

int P = {{p}};
int candidate_rrc_numbers = {{rrc_numbers}};
int ts_numbers = {{ts_numbers}};

range rrc_range = 1..candidate_rrc_numbers;
range ts_range = 1..ts_numbers;

int cost_df[ts_range][rrc_range] = ...;
int weight_ts[ts_range] = ...;
int rrc_max_load[rrc_range] = ...;
int rrc_selected_min_load[rrc_range] = ...;
int has_selected[rrc_range] = ...;

dvar boolean Xj[rrc_range];
dvar boolean Yij[ts_range][rrc_range];

minimize sum(ts in ts_range, rrc in rrc_range) cost_df[ts][rrc]*Yij[ts][rrc];  // Eq.1.1.最小化加权成本


subject to {
forall(ts in ts_range){
sum(rrc in rrc_range) Yij[ts][rrc] == 1;
}//  //Eq.1.2.每个TS有且仅有一个RRC服务

forall(ts in ts_range){
forall(rrc in rrc_range){
Yij[ts][rrc]<= Xj[rrc];
}}// Eq.1.3.如果RRC不开则不能服务

sum(rrc in rrc_range)Xj[rrc] == P;  //Eq.1.4.一共有P个RRC 

forall(rrc in rrc_range){
sum(ts in ts_range) weight_ts[ts]*Yij[ts][rrc]<= 1000*rrc_max_load[rrc];        // rrc_max_load千吨转成吨
}// Eq.1.2. RRC的服务上限

forall(rrc in rrc_range){
    if(has_selected[rrc]==1){
    //sum(ts in ts_range) weight_ts[ts]*Yij[ts][rrc]>= 1000*rrc_selected_min_load[rrc]; // rrc_min_load千吨转成吨
    Xj[rrc]==1;
    }

}

}


execute{
    var outfile = new IloOplOutputFile("r_Yij.csv");
    outfile.write("ts"+","+"rrc"+","+"decision Varibles"+'\n');
    for(var ts in ts_range){
        for(var rrc in rrc_range){
            outfile.write(ts+","+rrc+","+Yij[ts][rrc]+'\n');
    }}
    outfile.writeln();
    outfile.close();

    var outfile = new IloOplOutputFile("r_Xj.csv");
    outfile.write("rrc"+","+"decision Varibles"+'\n');
    for(var rrc in rrc_range){
        outfile.write(rrc+","+Xj[rrc]+'\n');
    }
    outfile.writeln();
    outfile.close();	

}        


