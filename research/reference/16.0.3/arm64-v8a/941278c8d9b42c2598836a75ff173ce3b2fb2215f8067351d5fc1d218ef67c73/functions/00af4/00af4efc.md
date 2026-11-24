# 00af4efc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00af3f08`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af3/00af3f08.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0028.md#compare-50fad1cf3e319d51fe3830e8529c4a76)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00af4efc",
  "name": "FUN_00af4efc",
  "size": 428,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "469d62adaf95a87a31593a3cc4f4f0a1da9ad7c7b7a7bca5609c8474ec3ee5c3",
  "source_text_sha256": "469d62adaf95a87a31593a3cc4f4f0a1da9ad7c7b7a7bca5609c8474ec3ee5c3",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00af4efc",
        "00af50a7"
      ]
    ],
    "bytes_sha256": "c58ed873dfd239a19566af7c46281e04d2d9bd04ef304b326c09f070d5df2eff",
    "instruction_count": 107,
    "instruction_bytes": 428,
    "body_bytes": 428,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [005f3680](../005f3/005f3680.md)
- [005f3e60](../005f3/005f3e60.md)
- [005f7d30](../005f7/005f7d30.md)
- [005f8c10](../005f8/005f8c10.md)
- [005f9aa0](../005f9/005f9aa0.md)
- [00707d34](../00707/00707d34.md)

## 呼び出し先

- [008524fc](../00852/008524fc.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1272 bytes

~~~c

bool FUN_00af4efc(int param_1,int param_2,int param_3)

{
  long lVar1;
  
  lVar1 = FUN_008524fc();
  if (((((*(int *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x848cc) != 0) &&
        (lVar1 = FUN_008524fc(),
        *(int *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x848cc) != 1)) &&
       (lVar1 = FUN_008524fc(),
       *(int *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x848cc) != 2)) &&
      ((lVar1 = FUN_008524fc(),
       *(int *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x848cc) != 0xb &&
       (lVar1 = FUN_008524fc(),
       *(int *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x848cc) != 0xd)))) &&
     (lVar1 = FUN_008524fc(),
     *(int *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x848cc) != 0x10)) {
    if ((param_3 == -1) ||
       (lVar1 = FUN_008524fc(),
       *(int *)(lVar1 + (long)param_1 * -0xc804 + (long)param_3 * 0x3ec + 0x913e4) == 0)) {
      return false;
    }
    lVar1 = FUN_008524fc();
    if (*(int *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x848cc) != 0xe) {
      lVar1 = FUN_008524fc();
      return *(int *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x848cc) == 0xf;
    }
  }
  return true;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00af4efc"></a> `00af4efc` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00af4f00"></a> `00af4f00` | `f5 0b 00 f9` | str x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00af4f04"></a> `00af4f04` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00af4f08"></a> `00af4f08` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00af4f0c"></a> `00af4f0c` | `f3 03 02 2a` | mov w19,w2 | `FALL_THROUGH`
<a id="insn-00af4f10"></a> `00af4f10` | `f4 03 01 2a` | mov w20,w1 | `FALL_THROUGH`
<a id="insn-00af4f14"></a> `00af4f14` | `f5 03 00 2a` | mov w21,w0 | `FALL_THROUGH`
<a id="insn-00af4f18"></a> `00af4f18` | `79 75 f5 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-00af4f1c"></a> `00af4f1c` | `88 00 99 52` | mov w8,#0xc804 | `FALL_THROUGH`
<a id="insn-00af4f20"></a> `00af4f20` | `89 7d 80 52` | mov w9,#0x3ec | `FALL_THROUGH`
<a id="insn-00af4f24"></a> `00af4f24` | `a8 02 28 9b` | smaddl x8,w21,w8,x0 | `FALL_THROUGH`
<a id="insn-00af4f28"></a> `00af4f28` | `88 22 29 9b` | smaddl x8,w20,w9,x8 | `FALL_THROUGH`
<a id="insn-00af4f2c"></a> `00af4f2c` | `89 19 89 52` | mov w9,#0x48cc | `FALL_THROUGH`
<a id="insn-00af4f30"></a> `00af4f30` | `09 01 a0 72` | movk w9,#0x8, LSL #16 | `FALL_THROUGH`
<a id="insn-00af4f34"></a> `00af4f34` | `08 69 69 b8` | ldr w8,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00af4f38"></a> `00af4f38` | `a8 06 00 34` | cbz w8,0x00af500c | `CONDITIONAL_JUMP`
<a id="insn-00af4f3c"></a> `00af4f3c` | `b5 7e 40 93` | sxtw x21,w21 | `FALL_THROUGH`
<a id="insn-00af4f40"></a> `00af4f40` | `94 7e 40 93` | sxtw x20,w20 | `FALL_THROUGH`
<a id="insn-00af4f44"></a> `00af4f44` | `6e 75 f5 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-00af4f48"></a> `00af4f48` | `88 00 99 52` | mov w8,#0xc804 | `FALL_THROUGH`
<a id="insn-00af4f4c"></a> `00af4f4c` | `89 7d 80 52` | mov w9,#0x3ec | `FALL_THROUGH`
<a id="insn-00af4f50"></a> `00af4f50` | `a8 02 28 9b` | smaddl x8,w21,w8,x0 | `FALL_THROUGH`
<a id="insn-00af4f54"></a> `00af4f54` | `88 22 29 9b` | smaddl x8,w20,w9,x8 | `FALL_THROUGH`
<a id="insn-00af4f58"></a> `00af4f58` | `89 19 89 52` | mov w9,#0x48cc | `FALL_THROUGH`
<a id="insn-00af4f5c"></a> `00af4f5c` | `09 01 a0 72` | movk w9,#0x8, LSL #16 | `FALL_THROUGH`
<a id="insn-00af4f60"></a> `00af4f60` | `08 69 69 b8` | ldr w8,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00af4f64"></a> `00af4f64` | `1f 05 00 71` | cmp w8,#0x1 | `FALL_THROUGH`
<a id="insn-00af4f68"></a> `00af4f68` | `20 05 00 54` | b.eq 0x00af500c | `CONDITIONAL_JUMP`
<a id="insn-00af4f6c"></a> `00af4f6c` | `64 75 f5 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-00af4f70"></a> `00af4f70` | `88 00 99 52` | mov w8,#0xc804 | `FALL_THROUGH`
<a id="insn-00af4f74"></a> `00af4f74` | `89 7d 80 52` | mov w9,#0x3ec | `FALL_THROUGH`
<a id="insn-00af4f78"></a> `00af4f78` | `a8 02 28 9b` | smaddl x8,w21,w8,x0 | `FALL_THROUGH`
<a id="insn-00af4f7c"></a> `00af4f7c` | `88 22 29 9b` | smaddl x8,w20,w9,x8 | `FALL_THROUGH`
<a id="insn-00af4f80"></a> `00af4f80` | `89 19 89 52` | mov w9,#0x48cc | `FALL_THROUGH`
<a id="insn-00af4f84"></a> `00af4f84` | `09 01 a0 72` | movk w9,#0x8, LSL #16 | `FALL_THROUGH`
<a id="insn-00af4f88"></a> `00af4f88` | `08 69 69 b8` | ldr w8,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00af4f8c"></a> `00af4f8c` | `1f 09 00 71` | cmp w8,#0x2 | `FALL_THROUGH`
<a id="insn-00af4f90"></a> `00af4f90` | `e0 03 00 54` | b.eq 0x00af500c | `CONDITIONAL_JUMP`
<a id="insn-00af4f94"></a> `00af4f94` | `5a 75 f5 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-00af4f98"></a> `00af4f98` | `88 00 99 52` | mov w8,#0xc804 | `FALL_THROUGH`
<a id="insn-00af4f9c"></a> `00af4f9c` | `89 7d 80 52` | mov w9,#0x3ec | `FALL_THROUGH`
<a id="insn-00af4fa0"></a> `00af4fa0` | `a8 02 28 9b` | smaddl x8,w21,w8,x0 | `FALL_THROUGH`
<a id="insn-00af4fa4"></a> `00af4fa4` | `88 22 29 9b` | smaddl x8,w20,w9,x8 | `FALL_THROUGH`
<a id="insn-00af4fa8"></a> `00af4fa8` | `89 19 89 52` | mov w9,#0x48cc | `FALL_THROUGH`
<a id="insn-00af4fac"></a> `00af4fac` | `09 01 a0 72` | movk w9,#0x8, LSL #16 | `FALL_THROUGH`
<a id="insn-00af4fb0"></a> `00af4fb0` | `08 69 69 b8` | ldr w8,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00af4fb4"></a> `00af4fb4` | `1f 2d 00 71` | cmp w8,#0xb | `FALL_THROUGH`
<a id="insn-00af4fb8"></a> `00af4fb8` | `a0 02 00 54` | b.eq 0x00af500c | `CONDITIONAL_JUMP`
<a id="insn-00af4fbc"></a> `00af4fbc` | `50 75 f5 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-00af4fc0"></a> `00af4fc0` | `88 00 99 52` | mov w8,#0xc804 | `FALL_THROUGH`
<a id="insn-00af4fc4"></a> `00af4fc4` | `89 7d 80 52` | mov w9,#0x3ec | `FALL_THROUGH`
<a id="insn-00af4fc8"></a> `00af4fc8` | `a8 02 28 9b` | smaddl x8,w21,w8,x0 | `FALL_THROUGH`
<a id="insn-00af4fcc"></a> `00af4fcc` | `88 22 29 9b` | smaddl x8,w20,w9,x8 | `FALL_THROUGH`
<a id="insn-00af4fd0"></a> `00af4fd0` | `89 19 89 52` | mov w9,#0x48cc | `FALL_THROUGH`
<a id="insn-00af4fd4"></a> `00af4fd4` | `09 01 a0 72` | movk w9,#0x8, LSL #16 | `FALL_THROUGH`
<a id="insn-00af4fd8"></a> `00af4fd8` | `08 69 69 b8` | ldr w8,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00af4fdc"></a> `00af4fdc` | `1f 35 00 71` | cmp w8,#0xd | `FALL_THROUGH`
<a id="insn-00af4fe0"></a> `00af4fe0` | `60 01 00 54` | b.eq 0x00af500c | `CONDITIONAL_JUMP`
<a id="insn-00af4fe4"></a> `00af4fe4` | `46 75 f5 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-00af4fe8"></a> `00af4fe8` | `88 00 99 52` | mov w8,#0xc804 | `FALL_THROUGH`
<a id="insn-00af4fec"></a> `00af4fec` | `89 7d 80 52` | mov w9,#0x3ec | `FALL_THROUGH`
<a id="insn-00af4ff0"></a> `00af4ff0` | `a8 02 28 9b` | smaddl x8,w21,w8,x0 | `FALL_THROUGH`
<a id="insn-00af4ff4"></a> `00af4ff4` | `88 22 29 9b` | smaddl x8,w20,w9,x8 | `FALL_THROUGH`
<a id="insn-00af4ff8"></a> `00af4ff8` | `89 19 89 52` | mov w9,#0x48cc | `FALL_THROUGH`
<a id="insn-00af4ffc"></a> `00af4ffc` | `09 01 a0 72` | movk w9,#0x8, LSL #16 | `FALL_THROUGH`
<a id="insn-00af5000"></a> `00af5000` | `08 69 69 b8` | ldr w8,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00af5004"></a> `00af5004` | `1f 41 00 71` | cmp w8,#0x10 | `FALL_THROUGH`
<a id="insn-00af5008"></a> `00af5008` | `c1 00 00 54` | b.ne 0x00af5020 | `CONDITIONAL_JUMP`
<a id="insn-00af500c"></a> `00af500c` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-00af5010"></a> `00af5010` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00af5014"></a> `00af5014` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00af5018"></a> `00af5018` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00af501c"></a> `00af501c` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00af5020"></a> `00af5020` | `7f 06 00 31` | cmn w19,#0x1 | `FALL_THROUGH`
<a id="insn-00af5024"></a> `00af5024` | `e0 03 00 54` | b.eq 0x00af50a0 | `CONDITIONAL_JUMP`
<a id="insn-00af5028"></a> `00af5028` | `35 75 f5 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-00af502c"></a> `00af502c` | `88 00 99 52` | mov w8,#0xc804 | `FALL_THROUGH`
<a id="insn-00af5030"></a> `00af5030` | `89 7d 80 52` | mov w9,#0x3ec | `FALL_THROUGH`
<a id="insn-00af5034"></a> `00af5034` | `a8 82 28 9b` | smsubl x8,w21,w8,x0 | `FALL_THROUGH`
<a id="insn-00af5038"></a> `00af5038` | `68 22 29 9b` | smaddl x8,w19,w9,x8 | `FALL_THROUGH`
<a id="insn-00af503c"></a> `00af503c` | `89 7c 82 52` | mov w9,#0x13e4 | `FALL_THROUGH`
<a id="insn-00af5040"></a> `00af5040` | `29 01 a0 72` | movk w9,#0x9, LSL #16 | `FALL_THROUGH`
<a id="insn-00af5044"></a> `00af5044` | `08 69 69 b8` | ldr w8,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00af5048"></a> `00af5048` | `c8 02 00 34` | cbz w8,0x00af50a0 | `CONDITIONAL_JUMP`
<a id="insn-00af504c"></a> `00af504c` | `2c 75 f5 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-00af5050"></a> `00af5050` | `88 00 99 52` | mov w8,#0xc804 | `FALL_THROUGH`
<a id="insn-00af5054"></a> `00af5054` | `89 7d 80 52` | mov w9,#0x3ec | `FALL_THROUGH`
<a id="insn-00af5058"></a> `00af5058` | `a8 02 28 9b` | smaddl x8,w21,w8,x0 | `FALL_THROUGH`
<a id="insn-00af505c"></a> `00af505c` | `88 22 29 9b` | smaddl x8,w20,w9,x8 | `FALL_THROUGH`
<a id="insn-00af5060"></a> `00af5060` | `89 19 89 52` | mov w9,#0x48cc | `FALL_THROUGH`
<a id="insn-00af5064"></a> `00af5064` | `09 01 a0 72` | movk w9,#0x8, LSL #16 | `FALL_THROUGH`
<a id="insn-00af5068"></a> `00af5068` | `08 69 69 b8` | ldr w8,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00af506c"></a> `00af506c` | `1f 39 00 71` | cmp w8,#0xe | `FALL_THROUGH`
<a id="insn-00af5070"></a> `00af5070` | `e0 fc ff 54` | b.eq 0x00af500c | `CONDITIONAL_JUMP`
<a id="insn-00af5074"></a> `00af5074` | `22 75 f5 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-00af5078"></a> `00af5078` | `88 00 99 52` | mov w8,#0xc804 | `FALL_THROUGH`
<a id="insn-00af507c"></a> `00af507c` | `89 7d 80 52` | mov w9,#0x3ec | `FALL_THROUGH`
<a id="insn-00af5080"></a> `00af5080` | `a8 02 28 9b` | smaddl x8,w21,w8,x0 | `FALL_THROUGH`
<a id="insn-00af5084"></a> `00af5084` | `88 22 29 9b` | smaddl x8,w20,w9,x8 | `FALL_THROUGH`
<a id="insn-00af5088"></a> `00af5088` | `89 19 89 52` | mov w9,#0x48cc | `FALL_THROUGH`
<a id="insn-00af508c"></a> `00af508c` | `09 01 a0 72` | movk w9,#0x8, LSL #16 | `FALL_THROUGH`
<a id="insn-00af5090"></a> `00af5090` | `08 69 69 b8` | ldr w8,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00af5094"></a> `00af5094` | `1f 3d 00 71` | cmp w8,#0xf | `FALL_THROUGH`
<a id="insn-00af5098"></a> `00af5098` | `e0 17 9f 1a` | cset w0,eq | `FALL_THROUGH`
<a id="insn-00af509c"></a> `00af509c` | `dd ff ff 17` | b 0x00af5010 | `UNCONDITIONAL_JUMP`
<a id="insn-00af50a0"></a> `00af50a0` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00af50a4"></a> `00af50a4` | `db ff ff 17` | b 0x00af5010 | `UNCONDITIONAL_JUMP`

## 基本ブロックと分岐先

- ブロック [`00af4efc`](#insn-00af4efc) 範囲 `[['00af4efc', '00af4f3b']]`
  - `CONDITIONAL_JUMP` [`00af4f38`](#insn-00af4f38) → [`00af500c`](#insn-00af500c)
  - `FALL_THROUGH` [`00af4f38`](#insn-00af4f38) → [`00af4f3c`](#insn-00af4f3c)
- ブロック [`00af4f3c`](#insn-00af4f3c) 範囲 `[['00af4f3c', '00af4f6b']]`
  - `CONDITIONAL_JUMP` [`00af4f68`](#insn-00af4f68) → [`00af500c`](#insn-00af500c)
  - `FALL_THROUGH` [`00af4f68`](#insn-00af4f68) → [`00af4f6c`](#insn-00af4f6c)
- ブロック [`00af4f6c`](#insn-00af4f6c) 範囲 `[['00af4f6c', '00af4f93']]`
  - `CONDITIONAL_JUMP` [`00af4f90`](#insn-00af4f90) → [`00af500c`](#insn-00af500c)
  - `FALL_THROUGH` [`00af4f90`](#insn-00af4f90) → [`00af4f94`](#insn-00af4f94)
- ブロック [`00af4f94`](#insn-00af4f94) 範囲 `[['00af4f94', '00af4fbb']]`
  - `CONDITIONAL_JUMP` [`00af4fb8`](#insn-00af4fb8) → [`00af500c`](#insn-00af500c)
  - `FALL_THROUGH` [`00af4fb8`](#insn-00af4fb8) → [`00af4fbc`](#insn-00af4fbc)
- ブロック [`00af4fbc`](#insn-00af4fbc) 範囲 `[['00af4fbc', '00af4fe3']]`
  - `CONDITIONAL_JUMP` [`00af4fe0`](#insn-00af4fe0) → [`00af500c`](#insn-00af500c)
  - `FALL_THROUGH` [`00af4fe0`](#insn-00af4fe0) → [`00af4fe4`](#insn-00af4fe4)
- ブロック [`00af4fe4`](#insn-00af4fe4) 範囲 `[['00af4fe4', '00af500b']]`
  - `CONDITIONAL_JUMP` [`00af5008`](#insn-00af5008) → [`00af5020`](#insn-00af5020)
  - `FALL_THROUGH` [`00af5008`](#insn-00af5008) → [`00af500c`](#insn-00af500c)
- ブロック [`00af500c`](#insn-00af500c) 範囲 `[['00af500c', '00af500f']]`
  - `FALL_THROUGH` [`00af500c`](#insn-00af500c) → [`00af5010`](#insn-00af5010)
- ブロック [`00af5010`](#insn-00af5010) 範囲 `[['00af5010', '00af501f']]`
- ブロック [`00af5020`](#insn-00af5020) 範囲 `[['00af5020', '00af5027']]`
  - `CONDITIONAL_JUMP` [`00af5024`](#insn-00af5024) → [`00af50a0`](#insn-00af50a0)
  - `FALL_THROUGH` [`00af5024`](#insn-00af5024) → [`00af5028`](#insn-00af5028)
- ブロック [`00af5028`](#insn-00af5028) 範囲 `[['00af5028', '00af504b']]`
  - `CONDITIONAL_JUMP` [`00af5048`](#insn-00af5048) → [`00af50a0`](#insn-00af50a0)
  - `FALL_THROUGH` [`00af5048`](#insn-00af5048) → [`00af504c`](#insn-00af504c)
- ブロック [`00af504c`](#insn-00af504c) 範囲 `[['00af504c', '00af5073']]`
  - `CONDITIONAL_JUMP` [`00af5070`](#insn-00af5070) → [`00af500c`](#insn-00af500c)
  - `FALL_THROUGH` [`00af5070`](#insn-00af5070) → [`00af5074`](#insn-00af5074)
- ブロック [`00af5074`](#insn-00af5074) 範囲 `[['00af5074', '00af509f']]`
  - `UNCONDITIONAL_JUMP` [`00af509c`](#insn-00af509c) → [`00af5010`](#insn-00af5010)
- ブロック [`00af50a0`](#insn-00af50a0) 範囲 `[['00af50a0', '00af50a7']]`
  - `UNCONDITIONAL_JUMP` [`00af50a4`](#insn-00af50a4) → [`00af5010`](#insn-00af5010)

## 命令位置別の参照

- [`00af4efc`](#insn-00af4efc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af4f00`](#insn-00af4f00) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af4f04`](#insn-00af4f04) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af4f18`](#insn-00af4f18) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`00af4f38`](#insn-00af4f38) → [`00af500c`](#insn-00af500c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af4f44`](#insn-00af4f44) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`00af4f68`](#insn-00af4f68) → [`00af500c`](#insn-00af500c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af4f6c`](#insn-00af4f6c) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`00af4f90`](#insn-00af4f90) → [`00af500c`](#insn-00af500c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af4f94`](#insn-00af4f94) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`00af4fb8`](#insn-00af4fb8) → [`00af500c`](#insn-00af500c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af4fbc`](#insn-00af4fbc) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`00af4fe0`](#insn-00af4fe0) → [`00af500c`](#insn-00af500c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af4fe4`](#insn-00af4fe4) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`00af5008`](#insn-00af5008) → [`00af5020`](#insn-00af5020) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af5010`](#insn-00af5010) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af5014`](#insn-00af5014) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af5018`](#insn-00af5018) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af5024`](#insn-00af5024) → [`00af50a0`](#insn-00af50a0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af5028`](#insn-00af5028) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`00af5048`](#insn-00af5048) → [`00af50a0`](#insn-00af50a0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af504c`](#insn-00af504c) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`00af5070`](#insn-00af5070) → [`00af500c`](#insn-00af500c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af5074`](#insn-00af5074) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`00af509c`](#insn-00af509c) → [`00af5010`](#insn-00af5010) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af50a4`](#insn-00af50a4) → [`00af5010`](#insn-00af5010) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00af4efc`](#insn-00af4efc)

~~~json
{
  "source": "00af4efc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af4f00`](#insn-00af4f00)

~~~json
{
  "source": "00af4f00",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af4f04`](#insn-00af4f04)

~~~json
{
  "source": "00af4f04",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af4f18`](#insn-00af4f18)

~~~json
{
  "source": "00af4f18",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af4f38`](#insn-00af4f38)

~~~json
{
  "source": "00af4f38",
  "target": "00af500c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af4f44`](#insn-00af4f44)

~~~json
{
  "source": "00af4f44",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af4f68`](#insn-00af4f68)

~~~json
{
  "source": "00af4f68",
  "target": "00af500c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af4f6c`](#insn-00af4f6c)

~~~json
{
  "source": "00af4f6c",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af4f90`](#insn-00af4f90)

~~~json
{
  "source": "00af4f90",
  "target": "00af500c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af4f94`](#insn-00af4f94)

~~~json
{
  "source": "00af4f94",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af4fb8`](#insn-00af4fb8)

~~~json
{
  "source": "00af4fb8",
  "target": "00af500c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af4fbc`](#insn-00af4fbc)

~~~json
{
  "source": "00af4fbc",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af4fe0`](#insn-00af4fe0)

~~~json
{
  "source": "00af4fe0",
  "target": "00af500c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af4fe4`](#insn-00af4fe4)

~~~json
{
  "source": "00af4fe4",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af5008`](#insn-00af5008)

~~~json
{
  "source": "00af5008",
  "target": "00af5020",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af5010`](#insn-00af5010)

~~~json
{
  "source": "00af5010",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af5014`](#insn-00af5014)

~~~json
{
  "source": "00af5014",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af5018`](#insn-00af5018)

~~~json
{
  "source": "00af5018",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af5024`](#insn-00af5024)

~~~json
{
  "source": "00af5024",
  "target": "00af50a0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af5028`](#insn-00af5028)

~~~json
{
  "source": "00af5028",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af5048`](#insn-00af5048)

~~~json
{
  "source": "00af5048",
  "target": "00af50a0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af504c`](#insn-00af504c)

~~~json
{
  "source": "00af504c",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af5070`](#insn-00af5070)

~~~json
{
  "source": "00af5070",
  "target": "00af500c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af5074`](#insn-00af5074)

~~~json
{
  "source": "00af5074",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af509c`](#insn-00af509c)

~~~json
{
  "source": "00af509c",
  "target": "00af5010",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af50a4`](#insn-00af50a4)

~~~json
{
  "source": "00af50a4",
  "target": "00af5010",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
