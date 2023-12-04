#! /usr/bin/env -S nix eval --file
let
  lib = (import <nixpkgs> {}).lib;
  txt = builtins.readFile ./input.txt;
  lines = lib.filter (line: line != "") (lib.splitString "\n" txt);
  match = re: v: let m = builtins.match re v; in if m == null then throw "${re} not matched: '${v}'" else m;
  max = a: b: if a > b then a else b;
  games = builtins.map (line:
    let
      m = match "Game ([0-9]+): (.*)" line;
      id = lib.toIntBase10 (builtins.elemAt m 0);
      rounds = lib.splitString "; " (builtins.elemAt m 1);
      maxs = builtins.foldl' (acc: balls:
        builtins.foldl' (acc: ball:
          let
            m = match "([0-9]+) (red|green|blue)" ball;
            n = lib.toIntBase10 (builtins.elemAt m 0);
            color = builtins.elemAt m 1;
          in
            (acc // {${color}=(max n acc.${color});})
        ) acc (lib.splitString ", " balls)
      ) {red=0; green=0; blue=0;} rounds;
    in
      {id=id; valid= maxs.red <= 12 && maxs.green <= 13 && maxs.blue <= 14;}
  ) lines;
  validGames = lib.filter (g: g.valid) games;
in
  lib.foldl' (acc: g: acc+g.id) 0 validGames
