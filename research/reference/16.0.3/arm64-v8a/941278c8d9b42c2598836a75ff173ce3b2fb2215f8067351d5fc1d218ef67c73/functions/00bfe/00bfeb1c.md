# 00bfeb1c

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bfdb28`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfd/00bfdb28.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0038.md#compare-9806d80f0f46720ca01727245bc2ea35)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bfeb1c",
  "name": "_ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE3getERNS_15basic_streambufIcS2_EEc",
  "size": 348,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "75fa039ae1fab26d146a1f6283555b1af5e8f93b24ab2e8825805856c648d1d3",
  "source_text_sha256": "75fa039ae1fab26d146a1f6283555b1af5e8f93b24ab2e8825805856c648d1d3",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bfeb1c",
        "00bfec77"
      ]
    ],
    "bytes_sha256": "3427baae86cd1e472dbabdb2fca31996ba901e133a0b529e0ad504f90c01733b",
    "instruction_count": 87,
    "instruction_bytes": 348,
    "body_bytes": 348,
    "indirect": 3,
    "unresolved": 3
  }
}
~~~

## 呼び出し元

- [00c5f420](../00c5f/00c5f420.md)

## 呼び出し先

- [00c59340](../00c59/00c59340.md)
- [00c5ae70](../00c5a/00c5ae70.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1699 bytes

~~~c

long * _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE3getERNS_15basic_streambufIcS2_EEc
                 (long *param_1,long *param_2,uint param_3)

{
  long lVar1;
  uint uVar2;
  undefined1 *puVar3;
  uint uVar4;
  int iVar5;
  long *plVar6;
  char local_24 [4];
  
  param_1[1] = 0;
  _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE6sentryC1ERS3_b(local_24,param_1,1);
  if (local_24[0] != '\0') {
    while( true ) {
      plVar6 = *(long **)((long)param_1 + *(long *)(*param_1 + -0x18) + 0x28);
      if ((byte *)plVar6[3] == (byte *)plVar6[4]) {
        uVar4 = (**(code **)(*plVar6 + 0x48))();
        if (uVar4 == 0xffffffff) {
          uVar4 = 2;
          goto LAB_00bfec38;
        }
      }
      else {
        uVar4 = (uint)*(byte *)plVar6[3];
      }
      if ((uVar4 & 0xff) == (param_3 & 0xff)) break;
      puVar3 = (undefined1 *)param_2[6];
      if (puVar3 == (undefined1 *)param_2[7]) {
        iVar5 = (**(code **)(*param_2 + 0x68))(param_2,uVar4 & 0xff);
        if (iVar5 == -1) break;
      }
      else {
        param_2[6] = (long)(puVar3 + 1);
        *puVar3 = (char)uVar4;
      }
      if (param_1[1] != 0x7fffffffffffffff) {
        param_1[1] = param_1[1] + 1;
      }
      plVar6 = *(long **)((long)param_1 + *(long *)(*param_1 + -0x18) + 0x28);
      if (plVar6[3] == plVar6[4]) {
        (**(code **)(*plVar6 + 0x50))();
      }
      else {
        plVar6[3] = plVar6[3] + 1;
      }
    }
    uVar4 = 0;
LAB_00bfec38:
    lVar1 = (long)param_1 + *(long *)(*param_1 + -0x18);
    uVar2 = uVar4 | 4;
    if (param_1[1] != 0) {
      uVar2 = uVar4;
    }
    _ZNSt6__ndk18ios_base5clearEj(lVar1,*(uint *)(lVar1 + 0x20) | uVar2);
  }
  return param_1;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bfeb1c"></a> `00bfeb1c` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bfeb20"></a> `00bfeb20` | `fd 7b bc a9` | stp x29,x30,[sp, #-0x40]! | `FALL_THROUGH`
<a id="insn-00bfeb24"></a> `00bfeb24` | `f7 0b 00 f9` | str x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfeb28"></a> `00bfeb28` | `f6 57 02 a9` | stp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bfeb2c"></a> `00bfeb2c` | `f4 4f 03 a9` | stp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bfeb30"></a> `00bfeb30` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bfeb34"></a> `00bfeb34` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bfeb38"></a> `00bfeb38` | `f5 03 02 2a` | mov w21,w2 | `FALL_THROUGH`
<a id="insn-00bfeb3c"></a> `00bfeb3c` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-00bfeb40"></a> `00bfeb40` | `1f 04 00 f9` | str xzr,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00bfeb44"></a> `00bfeb44` | `a0 73 00 91` | add x0,x29,#0x1c | `FALL_THROUGH`
<a id="insn-00bfeb48"></a> `00bfeb48` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bfeb4c"></a> `00bfeb4c` | `22 00 80 52` | mov w2,#0x1 | `FALL_THROUGH`
<a id="insn-00bfeb50"></a> `00bfeb50` | `c8 70 01 94` | bl 0x00c5ae70 | `UNCONDITIONAL_CALL`
<a id="insn-00bfeb54"></a> `00bfeb54` | `a8 73 40 39` | ldrb w8,[x29, #0x1c] | `FALL_THROUGH`
<a id="insn-00bfeb58"></a> `00bfeb58` | `28 08 00 34` | cbz w8,0x00bfec5c | `CONDITIONAL_JUMP`
<a id="insn-00bfeb5c"></a> `00bfeb5c` | `b5 1e 00 12` | and w21,w21,#0xff | `FALL_THROUGH`
<a id="insn-00bfeb60"></a> `00bfeb60` | `76 a2 00 91` | add x22,x19,#0x28 | `FALL_THROUGH`
<a id="insn-00bfeb64"></a> `00bfeb64` | `17 00 f0 92` | mov x23,#0x7fffffffffffffff | `FALL_THROUGH`
<a id="insn-00bfeb68"></a> `00bfeb68` | `09 00 00 14` | b 0x00bfeb8c | `UNCONDITIONAL_JUMP`
<a id="insn-00bfeb6c"></a> `00bfeb6c` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bfeb70"></a> `00bfeb70` | `08 81 5e f8` | ldur x8,[x8, #-0x18] | `FALL_THROUGH`
<a id="insn-00bfeb74"></a> `00bfeb74` | `c0 6a 68 f8` | ldr x0,[x22, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00bfeb78"></a> `00bfeb78` | `08 a4 41 a9` | ldp x8,x9,[x0, #0x18] | `FALL_THROUGH`
<a id="insn-00bfeb7c"></a> `00bfeb7c` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bfeb80"></a> `00bfeb80` | `e0 04 00 54` | b.eq 0x00bfec1c | `CONDITIONAL_JUMP`
<a id="insn-00bfeb84"></a> `00bfeb84` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bfeb88"></a> `00bfeb88` | `08 0c 00 f9` | str x8,[x0, #0x18] | `FALL_THROUGH`
<a id="insn-00bfeb8c"></a> `00bfeb8c` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bfeb90"></a> `00bfeb90` | `08 81 5e f8` | ldur x8,[x8, #-0x18] | `FALL_THROUGH`
<a id="insn-00bfeb94"></a> `00bfeb94` | `c0 6a 68 f8` | ldr x0,[x22, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00bfeb98"></a> `00bfeb98` | `08 a4 41 a9` | ldp x8,x9,[x0, #0x18] | `FALL_THROUGH`
<a id="insn-00bfeb9c"></a> `00bfeb9c` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bfeba0"></a> `00bfeba0` | `60 00 00 54` | b.eq 0x00bfebac | `CONDITIONAL_JUMP`
<a id="insn-00bfeba4"></a> `00bfeba4` | `00 01 40 39` | ldrb w0,[x8] | `FALL_THROUGH`
<a id="insn-00bfeba8"></a> `00bfeba8` | `06 00 00 14` | b 0x00bfebc0 | `UNCONDITIONAL_JUMP`
<a id="insn-00bfebac"></a> `00bfebac` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bfebb0"></a> `00bfebb0` | `08 25 40 f9` | ldr x8,[x8, #0x48] | `FALL_THROUGH`
<a id="insn-00bfebb4"></a> `00bfebb4` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bfebb8"></a> `00bfebb8` | `1f 04 00 31` | cmn w0,#0x1 | `FALL_THROUGH`
<a id="insn-00bfebbc"></a> `00bfebbc` | `c0 03 00 54` | b.eq 0x00bfec34 | `CONDITIONAL_JUMP`
<a id="insn-00bfebc0"></a> `00bfebc0` | `08 1c 00 12` | and w8,w0,#0xff | `FALL_THROUGH`
<a id="insn-00bfebc4"></a> `00bfebc4` | `1f 01 15 6b` | cmp w8,w21 | `FALL_THROUGH`
<a id="insn-00bfebc8"></a> `00bfebc8` | `20 03 00 54` | b.eq 0x00bfec2c | `CONDITIONAL_JUMP`
<a id="insn-00bfebcc"></a> `00bfebcc` | `89 2a 43 a9` | ldp x9,x10,[x20, #0x30] | `FALL_THROUGH`
<a id="insn-00bfebd0"></a> `00bfebd0` | `3f 01 0a eb` | cmp x9,x10 | `FALL_THROUGH`
<a id="insn-00bfebd4"></a> `00bfebd4` | `a0 00 00 54` | b.eq 0x00bfebe8 | `CONDITIONAL_JUMP`
<a id="insn-00bfebd8"></a> `00bfebd8` | `2a 05 00 91` | add x10,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bfebdc"></a> `00bfebdc` | `8a 1a 00 f9` | str x10,[x20, #0x30] | `FALL_THROUGH`
<a id="insn-00bfebe0"></a> `00bfebe0` | `28 01 00 39` | strb w8,[x9] | `FALL_THROUGH`
<a id="insn-00bfebe4"></a> `00bfebe4` | `08 00 00 14` | b 0x00bfec04 | `UNCONDITIONAL_JUMP`
<a id="insn-00bfebe8"></a> `00bfebe8` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00bfebec"></a> `00bfebec` | `08 35 40 f9` | ldr x8,[x8, #0x68] | `FALL_THROUGH`
<a id="insn-00bfebf0"></a> `00bfebf0` | `01 1c 00 12` | and w1,w0,#0xff | `FALL_THROUGH`
<a id="insn-00bfebf4"></a> `00bfebf4` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bfebf8"></a> `00bfebf8` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bfebfc"></a> `00bfebfc` | `1f 04 00 31` | cmn w0,#0x1 | `FALL_THROUGH`
<a id="insn-00bfec00"></a> `00bfec00` | `60 01 00 54` | b.eq 0x00bfec2c | `CONDITIONAL_JUMP`
<a id="insn-00bfec04"></a> `00bfec04` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bfec08"></a> `00bfec08` | `1f 01 17 eb` | cmp x8,x23 | `FALL_THROUGH`
<a id="insn-00bfec0c"></a> `00bfec0c` | `00 fb ff 54` | b.eq 0x00bfeb6c | `CONDITIONAL_JUMP`
<a id="insn-00bfec10"></a> `00bfec10` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bfec14"></a> `00bfec14` | `68 06 00 f9` | str x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bfec18"></a> `00bfec18` | `d5 ff ff 17` | b 0x00bfeb6c | `UNCONDITIONAL_JUMP`
<a id="insn-00bfec1c"></a> `00bfec1c` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bfec20"></a> `00bfec20` | `08 29 40 f9` | ldr x8,[x8, #0x50] | `FALL_THROUGH`
<a id="insn-00bfec24"></a> `00bfec24` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bfec28"></a> `00bfec28` | `d9 ff ff 17` | b 0x00bfeb8c | `UNCONDITIONAL_JUMP`
<a id="insn-00bfec2c"></a> `00bfec2c` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00bfec30"></a> `00bfec30` | `02 00 00 14` | b 0x00bfec38 | `UNCONDITIONAL_JUMP`
<a id="insn-00bfec34"></a> `00bfec34` | `48 00 80 52` | mov w8,#0x2 | `FALL_THROUGH`
<a id="insn-00bfec38"></a> `00bfec38` | `69 2a 40 a9` | ldp x9,x10,[x19] | `FALL_THROUGH`
<a id="insn-00bfec3c"></a> `00bfec3c` | `29 81 5e f8` | ldur x9,[x9, #-0x18] | `FALL_THROUGH`
<a id="insn-00bfec40"></a> `00bfec40` | `5f 01 00 f1` | cmp x10,#0x0 | `FALL_THROUGH`
<a id="insn-00bfec44"></a> `00bfec44` | `60 02 09 8b` | add x0,x19,x9 | `FALL_THROUGH`
<a id="insn-00bfec48"></a> `00bfec48` | `09 01 1e 32` | orr w9,w8,#0x4 | `FALL_THROUGH`
<a id="insn-00bfec4c"></a> `00bfec4c` | `0a 20 40 b9` | ldr w10,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00bfec50"></a> `00bfec50` | `28 01 88 1a` | csel w8,w9,w8,eq | `FALL_THROUGH`
<a id="insn-00bfec54"></a> `00bfec54` | `41 01 08 2a` | orr w1,w10,w8 | `FALL_THROUGH`
<a id="insn-00bfec58"></a> `00bfec58` | `ba 69 01 94` | bl 0x00c59340 | `UNCONDITIONAL_CALL`
<a id="insn-00bfec5c"></a> `00bfec5c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bfec60"></a> `00bfec60` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bfec64"></a> `00bfec64` | `f7 0b 40 f9` | ldr x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfec68"></a> `00bfec68` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bfec6c"></a> `00bfec6c` | `fd 7b c4 a8` | ldp x29,x30,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-00bfec70"></a> `00bfec70` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bfec74"></a> `00bfec74` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bfeb1c`](#insn-00bfeb1c) 範囲 `[['00bfeb1c', '00bfeb5b']]`
  - `CONDITIONAL_JUMP` [`00bfeb58`](#insn-00bfeb58) → [`00bfec5c`](#insn-00bfec5c)
  - `FALL_THROUGH` [`00bfeb58`](#insn-00bfeb58) → [`00bfeb5c`](#insn-00bfeb5c)
- ブロック [`00bfeb5c`](#insn-00bfeb5c) 範囲 `[['00bfeb5c', '00bfeb6b']]`
  - `UNCONDITIONAL_JUMP` [`00bfeb68`](#insn-00bfeb68) → [`00bfeb8c`](#insn-00bfeb8c)
- ブロック [`00bfeb6c`](#insn-00bfeb6c) 範囲 `[['00bfeb6c', '00bfeb83']]`
  - `CONDITIONAL_JUMP` [`00bfeb80`](#insn-00bfeb80) → [`00bfec1c`](#insn-00bfec1c)
  - `FALL_THROUGH` [`00bfeb80`](#insn-00bfeb80) → [`00bfeb84`](#insn-00bfeb84)
- ブロック [`00bfeb84`](#insn-00bfeb84) 範囲 `[['00bfeb84', '00bfeb8b']]`
  - `FALL_THROUGH` [`00bfeb88`](#insn-00bfeb88) → [`00bfeb8c`](#insn-00bfeb8c)
- ブロック [`00bfeb8c`](#insn-00bfeb8c) 範囲 `[['00bfeb8c', '00bfeba3']]`
  - `CONDITIONAL_JUMP` [`00bfeba0`](#insn-00bfeba0) → [`00bfebac`](#insn-00bfebac)
  - `FALL_THROUGH` [`00bfeba0`](#insn-00bfeba0) → [`00bfeba4`](#insn-00bfeba4)
- ブロック [`00bfeba4`](#insn-00bfeba4) 範囲 `[['00bfeba4', '00bfebab']]`
  - `UNCONDITIONAL_JUMP` [`00bfeba8`](#insn-00bfeba8) → [`00bfebc0`](#insn-00bfebc0)
- ブロック [`00bfebac`](#insn-00bfebac) 範囲 `[['00bfebac', '00bfebbf']]`
  - `CONDITIONAL_JUMP` [`00bfebbc`](#insn-00bfebbc) → [`00bfec34`](#insn-00bfec34)
  - `FALL_THROUGH` [`00bfebbc`](#insn-00bfebbc) → [`00bfebc0`](#insn-00bfebc0)
- ブロック [`00bfebc0`](#insn-00bfebc0) 範囲 `[['00bfebc0', '00bfebcb']]`
  - `CONDITIONAL_JUMP` [`00bfebc8`](#insn-00bfebc8) → [`00bfec2c`](#insn-00bfec2c)
  - `FALL_THROUGH` [`00bfebc8`](#insn-00bfebc8) → [`00bfebcc`](#insn-00bfebcc)
- ブロック [`00bfebcc`](#insn-00bfebcc) 範囲 `[['00bfebcc', '00bfebd7']]`
  - `CONDITIONAL_JUMP` [`00bfebd4`](#insn-00bfebd4) → [`00bfebe8`](#insn-00bfebe8)
  - `FALL_THROUGH` [`00bfebd4`](#insn-00bfebd4) → [`00bfebd8`](#insn-00bfebd8)
- ブロック [`00bfebd8`](#insn-00bfebd8) 範囲 `[['00bfebd8', '00bfebe7']]`
  - `UNCONDITIONAL_JUMP` [`00bfebe4`](#insn-00bfebe4) → [`00bfec04`](#insn-00bfec04)
- ブロック [`00bfebe8`](#insn-00bfebe8) 範囲 `[['00bfebe8', '00bfec03']]`
  - `CONDITIONAL_JUMP` [`00bfec00`](#insn-00bfec00) → [`00bfec2c`](#insn-00bfec2c)
  - `FALL_THROUGH` [`00bfec00`](#insn-00bfec00) → [`00bfec04`](#insn-00bfec04)
- ブロック [`00bfec04`](#insn-00bfec04) 範囲 `[['00bfec04', '00bfec0f']]`
  - `CONDITIONAL_JUMP` [`00bfec0c`](#insn-00bfec0c) → [`00bfeb6c`](#insn-00bfeb6c)
  - `FALL_THROUGH` [`00bfec0c`](#insn-00bfec0c) → [`00bfec10`](#insn-00bfec10)
- ブロック [`00bfec10`](#insn-00bfec10) 範囲 `[['00bfec10', '00bfec1b']]`
  - `UNCONDITIONAL_JUMP` [`00bfec18`](#insn-00bfec18) → [`00bfeb6c`](#insn-00bfeb6c)
- ブロック [`00bfec1c`](#insn-00bfec1c) 範囲 `[['00bfec1c', '00bfec2b']]`
  - `UNCONDITIONAL_JUMP` [`00bfec28`](#insn-00bfec28) → [`00bfeb8c`](#insn-00bfeb8c)
- ブロック [`00bfec2c`](#insn-00bfec2c) 範囲 `[['00bfec2c', '00bfec33']]`
  - `UNCONDITIONAL_JUMP` [`00bfec30`](#insn-00bfec30) → [`00bfec38`](#insn-00bfec38)
- ブロック [`00bfec34`](#insn-00bfec34) 範囲 `[['00bfec34', '00bfec37']]`
  - `FALL_THROUGH` [`00bfec34`](#insn-00bfec34) → [`00bfec38`](#insn-00bfec38)
- ブロック [`00bfec38`](#insn-00bfec38) 範囲 `[['00bfec38', '00bfec5b']]`
  - `FALL_THROUGH` [`00bfec58`](#insn-00bfec58) → [`00bfec5c`](#insn-00bfec5c)
- ブロック [`00bfec5c`](#insn-00bfec5c) 範囲 `[['00bfec5c', '00bfec77']]`

## 命令位置別の参照

- [`00bfeb20`](#insn-00bfeb20) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfeb24`](#insn-00bfeb24) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfeb28`](#insn-00bfeb28) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfeb2c`](#insn-00bfeb2c) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfeb50`](#insn-00bfeb50) → [`00c5ae70`](../00c5a/00c5ae70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ae70` · 推定シンボル `None` · 推定型 `None`
- [`00bfeb54`](#insn-00bfeb54) → `Stack[-0x24]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfeb58`](#insn-00bfeb58) → [`00bfec5c`](#insn-00bfec5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfeb68`](#insn-00bfeb68) → [`00bfeb8c`](#insn-00bfeb8c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfeb80`](#insn-00bfeb80) → [`00bfec1c`](#insn-00bfec1c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfeba0`](#insn-00bfeba0) → [`00bfebac`](#insn-00bfebac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfeba8`](#insn-00bfeba8) → [`00bfebc0`](#insn-00bfebc0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfebbc`](#insn-00bfebbc) → [`00bfec34`](#insn-00bfec34) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfebc8`](#insn-00bfebc8) → [`00bfec2c`](#insn-00bfec2c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfebd4`](#insn-00bfebd4) → [`00bfebe8`](#insn-00bfebe8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfebe4`](#insn-00bfebe4) → [`00bfec04`](#insn-00bfec04) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfec00`](#insn-00bfec00) → [`00bfec2c`](#insn-00bfec2c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfec0c`](#insn-00bfec0c) → [`00bfeb6c`](#insn-00bfeb6c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfec18`](#insn-00bfec18) → [`00bfeb6c`](#insn-00bfeb6c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfec28`](#insn-00bfec28) → [`00bfeb8c`](#insn-00bfeb8c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfec30`](#insn-00bfec30) → [`00bfec38`](#insn-00bfec38) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfec58`](#insn-00bfec58) → [`00c59340`](../00c59/00c59340.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59340` · 推定シンボル `None` · 推定型 `None`
- [`00bfec60`](#insn-00bfec60) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfec64`](#insn-00bfec64) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfec68`](#insn-00bfec68) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfec6c`](#insn-00bfec6c) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bfeb20`](#insn-00bfeb20)

~~~json
{
  "source": "00bfeb20",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfeb24`](#insn-00bfeb24)

~~~json
{
  "source": "00bfeb24",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfeb28`](#insn-00bfeb28)

~~~json
{
  "source": "00bfeb28",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfeb2c`](#insn-00bfeb2c)

~~~json
{
  "source": "00bfeb2c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfeb50`](#insn-00bfeb50)

~~~json
{
  "source": "00bfeb50",
  "target": "00c5ae70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfeb54`](#insn-00bfeb54)

~~~json
{
  "source": "00bfeb54",
  "target": "Stack[-0x24]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfeb58`](#insn-00bfeb58)

~~~json
{
  "source": "00bfeb58",
  "target": "00bfec5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfeb68`](#insn-00bfeb68)

~~~json
{
  "source": "00bfeb68",
  "target": "00bfeb8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfeb80`](#insn-00bfeb80)

~~~json
{
  "source": "00bfeb80",
  "target": "00bfec1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfeba0`](#insn-00bfeba0)

~~~json
{
  "source": "00bfeba0",
  "target": "00bfebac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfeba8`](#insn-00bfeba8)

~~~json
{
  "source": "00bfeba8",
  "target": "00bfebc0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfebbc`](#insn-00bfebbc)

~~~json
{
  "source": "00bfebbc",
  "target": "00bfec34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfebc8`](#insn-00bfebc8)

~~~json
{
  "source": "00bfebc8",
  "target": "00bfec2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfebd4`](#insn-00bfebd4)

~~~json
{
  "source": "00bfebd4",
  "target": "00bfebe8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfebe4`](#insn-00bfebe4)

~~~json
{
  "source": "00bfebe4",
  "target": "00bfec04",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfec00`](#insn-00bfec00)

~~~json
{
  "source": "00bfec00",
  "target": "00bfec2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfec0c`](#insn-00bfec0c)

~~~json
{
  "source": "00bfec0c",
  "target": "00bfeb6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfec18`](#insn-00bfec18)

~~~json
{
  "source": "00bfec18",
  "target": "00bfeb6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfec28`](#insn-00bfec28)

~~~json
{
  "source": "00bfec28",
  "target": "00bfeb8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfec30`](#insn-00bfec30)

~~~json
{
  "source": "00bfec30",
  "target": "00bfec38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfec58`](#insn-00bfec58)

~~~json
{
  "source": "00bfec58",
  "target": "00c59340",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfec60`](#insn-00bfec60)

~~~json
{
  "source": "00bfec60",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfec64`](#insn-00bfec64)

~~~json
{
  "source": "00bfec64",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfec68`](#insn-00bfec68)

~~~json
{
  "source": "00bfec68",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfec6c`](#insn-00bfec6c)

~~~json
{
  "source": "00bfec6c",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
