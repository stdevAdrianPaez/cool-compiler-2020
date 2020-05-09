
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'rightASSIGNleftDOTleftATleftNOTleftISVOIDleftSTARDIVleftPLUSMINUSleftLOWEREQLOWEREQUALleftLNOTARROW ASSIGN AT BOOL CASE CBRACKET CLASS COLON COMMA CPAREN DIV DOT ELSE EQUAL ESAC FI ID IF IN INHERITS INT ISVOID LET LNOT LOOP LOWER LOWEREQ MINUS NEW NOT OBRACKET OF OPAREN PLUS POOL SEMICOLON STAR STRING THEN TYPE WHILEprogram : class_listempty :class_list : def_class SEMICOLON class_list\n                  | def_class SEMICOLONdef_class : CLASS TYPE OBRACKET feature_list CBRACKET\n                  | CLASS TYPE INHERITS TYPE OBRACKET feature_list CBRACKETfeature_list : def_attr SEMICOLON feature_list\n                    | def_func SEMICOLON feature_list\n                    | emptydef_attr : ID COLON TYPE ASSIGN expr\n                | ID COLON TYPEdef_func : ID OPAREN params CPAREN COLON TYPE OBRACKET expr CBRACKETparams : param_listparams : emptyparam_list : param COMMA param_list\n                  | param emptyparam : ID COLON TYPEexpr : LET let_attrs IN expr\n            | CASE expr OF case_list ESAC\n            | IF expr THEN expr ELSE expr FI\n            | WHILE expr LOOP expr POOLexpr : ID ASSIGN exprexpr : expr AT TYPE DOT ID OPAREN arg_list CPAREN\n            | expr DOT ID OPAREN arg_list CPAREN\n            | ID OPAREN arg_list CPARENexpr : expr PLUS expr\n            | expr MINUS expr\n            | expr STAR expr\n            | expr DIV expr\n            | expr LOWER expr\n            | expr LOWEREQ expr\n            | expr EQUAL exprexpr : NOT expr\n            | ISVOID expr\n            | LNOT exprexpr : OPAREN expr CPARENexpr : atomlet_attrs : def_attr COMMA let_attrs\n                | def_attrcase_list : case_elem SEMICOLON case_list\n                 | case_elem SEMICOLONcase_elem : ID COLON TYPE ARROW exprarg_list : arg_list_ne\n                | emptyarg_list_ne : expr COMMA arg_list_ne\n                   | expr atom : INTatom : IDatom : NEW TYPEatom : blockatom :  BOOLatom : STRINGblock : OBRACKET block_list CBRACKETblock_list : expr SEMICOLON block_list\n                  | expr SEMICOLON'
    
_lr_action_items = {'CLASS':([0,5,],[4,4,]),'$end':([1,2,5,7,],[0,-1,-4,-3,]),'SEMICOLON':([3,11,12,16,24,36,37,38,47,48,50,51,52,75,76,77,78,80,82,89,90,91,92,93,94,95,101,102,105,109,112,121,125,126,128,134,135,136,],[5,17,18,-5,-11,-6,-48,-10,-37,-47,-50,-51,-52,-33,-34,-35,-49,103,-22,-26,-27,-28,-29,-30,-31,-32,-36,-53,-25,-18,122,-19,-21,-12,-24,-20,-23,-42,]),'TYPE':([4,9,19,32,49,55,59,123,],[6,15,24,54,78,81,87,130,]),'OBRACKET':([6,15,31,40,41,42,43,44,45,46,53,57,58,61,62,63,64,65,66,67,81,96,99,100,103,104,106,108,124,127,133,],[8,21,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,104,53,53,53,53,53,53,53,53,53,53,]),'INHERITS':([6,],[9,]),'ID':([8,17,18,20,21,31,34,39,40,41,42,43,44,45,46,53,57,58,60,61,62,63,64,65,66,67,96,97,98,99,100,103,104,106,107,108,122,124,127,133,],[14,14,14,25,14,37,25,70,37,37,37,37,37,37,37,37,37,37,88,37,37,37,37,37,37,37,37,70,113,37,37,37,37,37,119,37,113,37,37,37,]),'CBRACKET':([8,10,13,17,18,21,22,23,30,37,47,48,50,51,52,75,76,77,78,79,82,89,90,91,92,93,94,95,101,102,103,105,109,116,117,121,125,128,134,135,],[-2,16,-9,-2,-2,-2,-7,-8,36,-48,-37,-47,-50,-51,-52,-33,-34,-35,-49,102,-22,-26,-27,-28,-29,-30,-31,-32,-36,-53,-55,-25,-18,-54,126,-19,-21,-24,-20,-23,]),'COLON':([14,25,33,70,113,],[19,32,55,19,123,]),'OPAREN':([14,31,37,40,41,42,43,44,45,46,53,57,58,61,62,63,64,65,66,67,88,96,99,100,103,104,106,108,119,124,127,133,],[20,43,58,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,108,43,43,43,43,43,43,43,127,43,43,43,]),'CPAREN':([20,26,27,28,29,35,37,47,48,50,51,52,54,56,58,74,75,76,77,78,82,83,84,85,86,89,90,91,92,93,94,95,101,102,105,108,109,118,120,121,125,127,128,132,134,135,],[-2,33,-13,-14,-2,-16,-48,-37,-47,-50,-51,-52,-17,-15,-2,101,-33,-34,-35,-49,-22,105,-43,-44,-46,-26,-27,-28,-29,-30,-31,-32,-36,-53,-25,-2,-18,-45,128,-19,-21,-2,-24,135,-20,-23,]),'ASSIGN':([24,37,],[31,57,]),'COMMA':([24,29,37,38,47,48,50,51,52,54,69,75,76,77,78,82,86,89,90,91,92,93,94,95,101,102,105,109,121,125,128,134,135,],[-11,34,-48,-10,-37,-47,-50,-51,-52,-17,97,-33,-34,-35,-49,-22,106,-26,-27,-28,-29,-30,-31,-32,-36,-53,-25,-18,-19,-21,-24,-20,-23,]),'IN':([24,37,38,47,48,50,51,52,68,69,75,76,77,78,82,89,90,91,92,93,94,95,101,102,105,109,110,121,125,128,134,135,],[-11,-48,-10,-37,-47,-50,-51,-52,96,-39,-33,-34,-35,-49,-22,-26,-27,-28,-29,-30,-31,-32,-36,-53,-25,-18,-38,-19,-21,-24,-20,-23,]),'LET':([31,40,41,42,43,44,45,46,53,57,58,61,62,63,64,65,66,67,96,99,100,103,104,106,108,124,127,133,],[39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,]),'CASE':([31,40,41,42,43,44,45,46,53,57,58,61,62,63,64,65,66,67,96,99,100,103,104,106,108,124,127,133,],[40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,]),'IF':([31,40,41,42,43,44,45,46,53,57,58,61,62,63,64,65,66,67,96,99,100,103,104,106,108,124,127,133,],[41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,]),'WHILE':([31,40,41,42,43,44,45,46,53,57,58,61,62,63,64,65,66,67,96,99,100,103,104,106,108,124,127,133,],[42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,]),'NOT':([31,40,41,42,43,44,45,46,53,57,58,61,62,63,64,65,66,67,96,99,100,103,104,106,108,124,127,133,],[44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,]),'ISVOID':([31,40,41,42,43,44,45,46,53,57,58,61,62,63,64,65,66,67,96,99,100,103,104,106,108,124,127,133,],[45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,]),'LNOT':([31,40,41,42,43,44,45,46,53,57,58,61,62,63,64,65,66,67,96,99,100,103,104,106,108,124,127,133,],[46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,]),'INT':([31,40,41,42,43,44,45,46,53,57,58,61,62,63,64,65,66,67,96,99,100,103,104,106,108,124,127,133,],[48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,]),'NEW':([31,40,41,42,43,44,45,46,53,57,58,61,62,63,64,65,66,67,96,99,100,103,104,106,108,124,127,133,],[49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,]),'BOOL':([31,40,41,42,43,44,45,46,53,57,58,61,62,63,64,65,66,67,96,99,100,103,104,106,108,124,127,133,],[51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,]),'STRING':([31,40,41,42,43,44,45,46,53,57,58,61,62,63,64,65,66,67,96,99,100,103,104,106,108,124,127,133,],[52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,]),'AT':([37,38,47,48,50,51,52,71,72,73,74,75,76,77,78,80,82,86,89,90,91,92,93,94,95,101,102,105,109,114,115,117,121,125,128,131,134,135,136,],[-48,59,-37,-47,-50,-51,-52,59,59,59,59,-33,-34,-35,-49,59,59,59,-26,-27,-28,-29,-30,-31,-32,-36,-53,-25,59,59,59,59,-19,-21,-24,59,-20,-23,59,]),'DOT':([37,38,47,48,50,51,52,71,72,73,74,75,76,77,78,80,82,86,87,89,90,91,92,93,94,95,101,102,105,109,114,115,117,121,125,128,131,134,135,136,],[-48,60,-37,-47,-50,-51,-52,60,60,60,60,-33,-34,-35,-49,60,60,60,107,-26,-27,-28,-29,-30,-31,-32,-36,-53,-25,60,60,60,60,-19,-21,-24,60,-20,-23,60,]),'PLUS':([37,38,47,48,50,51,52,71,72,73,74,75,76,77,78,80,82,86,89,90,91,92,93,94,95,101,102,105,109,114,115,117,121,125,128,131,134,135,136,],[-48,61,-37,-47,-50,-51,-52,61,61,61,61,61,61,-35,-49,61,61,61,-26,-27,61,61,-30,-31,-32,-36,-53,-25,61,61,61,61,-19,-21,-24,61,-20,-23,61,]),'MINUS':([37,38,47,48,50,51,52,71,72,73,74,75,76,77,78,80,82,86,89,90,91,92,93,94,95,101,102,105,109,114,115,117,121,125,128,131,134,135,136,],[-48,62,-37,-47,-50,-51,-52,62,62,62,62,62,62,-35,-49,62,62,62,-26,-27,62,62,-30,-31,-32,-36,-53,-25,62,62,62,62,-19,-21,-24,62,-20,-23,62,]),'STAR':([37,38,47,48,50,51,52,71,72,73,74,75,76,77,78,80,82,86,89,90,91,92,93,94,95,101,102,105,109,114,115,117,121,125,128,131,134,135,136,],[-48,63,-37,-47,-50,-51,-52,63,63,63,63,63,63,-35,-49,63,63,63,-26,-27,-28,-29,-30,-31,-32,-36,-53,-25,63,63,63,63,-19,-21,-24,63,-20,-23,63,]),'DIV':([37,38,47,48,50,51,52,71,72,73,74,75,76,77,78,80,82,86,89,90,91,92,93,94,95,101,102,105,109,114,115,117,121,125,128,131,134,135,136,],[-48,64,-37,-47,-50,-51,-52,64,64,64,64,64,64,-35,-49,64,64,64,-26,-27,-28,-29,-30,-31,-32,-36,-53,-25,64,64,64,64,-19,-21,-24,64,-20,-23,64,]),'LOWER':([37,38,47,48,50,51,52,71,72,73,74,75,76,77,78,80,82,86,89,90,91,92,93,94,95,101,102,105,109,114,115,117,121,125,128,131,134,135,136,],[-48,65,-37,-47,-50,-51,-52,65,65,65,65,65,65,-35,-49,65,65,65,65,65,65,65,-30,-31,-32,-36,-53,-25,65,65,65,65,-19,-21,-24,65,-20,-23,65,]),'LOWEREQ':([37,38,47,48,50,51,52,71,72,73,74,75,76,77,78,80,82,86,89,90,91,92,93,94,95,101,102,105,109,114,115,117,121,125,128,131,134,135,136,],[-48,66,-37,-47,-50,-51,-52,66,66,66,66,66,66,-35,-49,66,66,66,66,66,66,66,-30,-31,-32,-36,-53,-25,66,66,66,66,-19,-21,-24,66,-20,-23,66,]),'EQUAL':([37,38,47,48,50,51,52,71,72,73,74,75,76,77,78,80,82,86,89,90,91,92,93,94,95,101,102,105,109,114,115,117,121,125,128,131,134,135,136,],[-48,67,-37,-47,-50,-51,-52,67,67,67,67,67,67,-35,-49,67,67,67,67,67,67,67,-30,-31,-32,-36,-53,-25,67,67,67,67,-19,-21,-24,67,-20,-23,67,]),'OF':([37,47,48,50,51,52,71,75,76,77,78,82,89,90,91,92,93,94,95,101,102,105,109,121,125,128,134,135,],[-48,-37,-47,-50,-51,-52,98,-33,-34,-35,-49,-22,-26,-27,-28,-29,-30,-31,-32,-36,-53,-25,-18,-19,-21,-24,-20,-23,]),'THEN':([37,47,48,50,51,52,72,75,76,77,78,82,89,90,91,92,93,94,95,101,102,105,109,121,125,128,134,135,],[-48,-37,-47,-50,-51,-52,99,-33,-34,-35,-49,-22,-26,-27,-28,-29,-30,-31,-32,-36,-53,-25,-18,-19,-21,-24,-20,-23,]),'LOOP':([37,47,48,50,51,52,73,75,76,77,78,82,89,90,91,92,93,94,95,101,102,105,109,121,125,128,134,135,],[-48,-37,-47,-50,-51,-52,100,-33,-34,-35,-49,-22,-26,-27,-28,-29,-30,-31,-32,-36,-53,-25,-18,-19,-21,-24,-20,-23,]),'ELSE':([37,47,48,50,51,52,75,76,77,78,82,89,90,91,92,93,94,95,101,102,105,109,114,121,125,128,134,135,],[-48,-37,-47,-50,-51,-52,-33,-34,-35,-49,-22,-26,-27,-28,-29,-30,-31,-32,-36,-53,-25,-18,124,-19,-21,-24,-20,-23,]),'POOL':([37,47,48,50,51,52,75,76,77,78,82,89,90,91,92,93,94,95,101,102,105,109,115,121,125,128,134,135,],[-48,-37,-47,-50,-51,-52,-33,-34,-35,-49,-22,-26,-27,-28,-29,-30,-31,-32,-36,-53,-25,-18,125,-19,-21,-24,-20,-23,]),'FI':([37,47,48,50,51,52,75,76,77,78,82,89,90,91,92,93,94,95,101,102,105,109,121,125,128,131,134,135,],[-48,-37,-47,-50,-51,-52,-33,-34,-35,-49,-22,-26,-27,-28,-29,-30,-31,-32,-36,-53,-25,-18,-19,-21,-24,134,-20,-23,]),'ESAC':([111,122,129,],[121,-41,-40,]),'ARROW':([130,],[133,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'class_list':([0,5,],[2,7,]),'def_class':([0,5,],[3,3,]),'feature_list':([8,17,18,21,],[10,22,23,30,]),'def_attr':([8,17,18,21,39,97,],[11,11,11,11,69,69,]),'def_func':([8,17,18,21,],[12,12,12,12,]),'empty':([8,17,18,20,21,29,58,108,127,],[13,13,13,28,13,35,85,85,85,]),'params':([20,],[26,]),'param_list':([20,34,],[27,56,]),'param':([20,34,],[29,29,]),'expr':([31,40,41,42,43,44,45,46,53,57,58,61,62,63,64,65,66,67,96,99,100,103,104,106,108,124,127,133,],[38,71,72,73,74,75,76,77,80,82,86,89,90,91,92,93,94,95,109,114,115,80,117,86,86,131,86,136,]),'atom':([31,40,41,42,43,44,45,46,53,57,58,61,62,63,64,65,66,67,96,99,100,103,104,106,108,124,127,133,],[47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,]),'block':([31,40,41,42,43,44,45,46,53,57,58,61,62,63,64,65,66,67,96,99,100,103,104,106,108,124,127,133,],[50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,]),'let_attrs':([39,97,],[68,110,]),'block_list':([53,103,],[79,116,]),'arg_list':([58,108,127,],[83,120,132,]),'arg_list_ne':([58,106,108,127,],[84,118,84,84,]),'case_list':([98,122,],[111,129,]),'case_elem':([98,122,],[112,112,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> class_list','program',1,'p_program','parser.py',21),
  ('empty -> <empty>','empty',0,'p_empty','parser.py',26),
  ('class_list -> def_class SEMICOLON class_list','class_list',3,'p_class_list','parser.py',31),
  ('class_list -> def_class SEMICOLON','class_list',2,'p_class_list','parser.py',32),
  ('def_class -> CLASS TYPE OBRACKET feature_list CBRACKET','def_class',5,'p_def_class','parser.py',41),
  ('def_class -> CLASS TYPE INHERITS TYPE OBRACKET feature_list CBRACKET','def_class',7,'p_def_class','parser.py',42),
  ('feature_list -> def_attr SEMICOLON feature_list','feature_list',3,'p_feature_list','parser.py',52),
  ('feature_list -> def_func SEMICOLON feature_list','feature_list',3,'p_feature_list','parser.py',53),
  ('feature_list -> empty','feature_list',1,'p_feature_list','parser.py',54),
  ('def_attr -> ID COLON TYPE ASSIGN expr','def_attr',5,'p_def_attr_declaration','parser.py',62),
  ('def_attr -> ID COLON TYPE','def_attr',3,'p_def_attr_declaration','parser.py',63),
  ('def_func -> ID OPAREN params CPAREN COLON TYPE OBRACKET expr CBRACKET','def_func',9,'p_def_func','parser.py',73),
  ('params -> param_list','params',1,'p_params_ne','parser.py',79),
  ('params -> empty','params',1,'p_params_e','parser.py',84),
  ('param_list -> param COMMA param_list','param_list',3,'p_param_list','parser.py',89),
  ('param_list -> param empty','param_list',2,'p_param_list','parser.py',90),
  ('param -> ID COLON TYPE','param',3,'p_param','parser.py',98),
  ('expr -> LET let_attrs IN expr','expr',4,'p_expr_flow','parser.py',104),
  ('expr -> CASE expr OF case_list ESAC','expr',5,'p_expr_flow','parser.py',105),
  ('expr -> IF expr THEN expr ELSE expr FI','expr',7,'p_expr_flow','parser.py',106),
  ('expr -> WHILE expr LOOP expr POOL','expr',5,'p_expr_flow','parser.py',107),
  ('expr -> ID ASSIGN expr','expr',3,'p_expr_assign','parser.py',122),
  ('expr -> expr AT TYPE DOT ID OPAREN arg_list CPAREN','expr',8,'p_expr_func_all','parser.py',128),
  ('expr -> expr DOT ID OPAREN arg_list CPAREN','expr',6,'p_expr_func_all','parser.py',129),
  ('expr -> ID OPAREN arg_list CPAREN','expr',4,'p_expr_func_all','parser.py',130),
  ('expr -> expr PLUS expr','expr',3,'p_expr_operators_binary','parser.py',151),
  ('expr -> expr MINUS expr','expr',3,'p_expr_operators_binary','parser.py',152),
  ('expr -> expr STAR expr','expr',3,'p_expr_operators_binary','parser.py',153),
  ('expr -> expr DIV expr','expr',3,'p_expr_operators_binary','parser.py',154),
  ('expr -> expr LOWER expr','expr',3,'p_expr_operators_binary','parser.py',155),
  ('expr -> expr LOWEREQ expr','expr',3,'p_expr_operators_binary','parser.py',156),
  ('expr -> expr EQUAL expr','expr',3,'p_expr_operators_binary','parser.py',157),
  ('expr -> NOT expr','expr',2,'p_expr_operators_unary','parser.py',177),
  ('expr -> ISVOID expr','expr',2,'p_expr_operators_unary','parser.py',178),
  ('expr -> LNOT expr','expr',2,'p_expr_operators_unary','parser.py',179),
  ('expr -> OPAREN expr CPAREN','expr',3,'p_expr_group','parser.py',191),
  ('expr -> atom','expr',1,'p_expr_atom','parser.py',196),
  ('let_attrs -> def_attr COMMA let_attrs','let_attrs',3,'p_let_attrs','parser.py',201),
  ('let_attrs -> def_attr','let_attrs',1,'p_let_attrs','parser.py',202),
  ('case_list -> case_elem SEMICOLON case_list','case_list',3,'p_case_list','parser.py',210),
  ('case_list -> case_elem SEMICOLON','case_list',2,'p_case_list','parser.py',211),
  ('case_elem -> ID COLON TYPE ARROW expr','case_elem',5,'p_case_elem','parser.py',219),
  ('arg_list -> arg_list_ne','arg_list',1,'p_arg_list','parser.py',225),
  ('arg_list -> empty','arg_list',1,'p_arg_list','parser.py',226),
  ('arg_list_ne -> expr COMMA arg_list_ne','arg_list_ne',3,'p_arg_list_ne','parser.py',231),
  ('arg_list_ne -> expr','arg_list_ne',1,'p_arg_list_ne','parser.py',232),
  ('atom -> INT','atom',1,'p_atom_int','parser.py',240),
  ('atom -> ID','atom',1,'p_atom_id','parser.py',246),
  ('atom -> NEW TYPE','atom',2,'p_atom_new','parser.py',252),
  ('atom -> block','atom',1,'p_atom_block','parser.py',258),
  ('atom -> BOOL','atom',1,'p_atom_bool','parser.py',263),
  ('atom -> STRING','atom',1,'p_atom_atring','parser.py',269),
  ('block -> OBRACKET block_list CBRACKET','block',3,'p_block','parser.py',275),
  ('block_list -> expr SEMICOLON block_list','block_list',3,'p_block_list','parser.py',280),
  ('block_list -> expr SEMICOLON','block_list',2,'p_block_list','parser.py',281),
]
