# 00baacb8

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00ba9cc4`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba9/00ba9cc4.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0035.md#compare-673836e5514fa4aab8ec55da2d82cfad)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00baacb8",
  "name": "_ZNKSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers8FieldDefEEENS_19__map_value_compareIS7_SB_NS_4lessIS7_EELb1EEENS5_ISB_EEE4findIS7_EENS_21__tree_const_iteratorISB_PNS_11__tree_nodeISB_PvEElEERKT_",
  "size": 276,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "10cb4109329cef5b1ccc26c0456d49d122c6a4e7cdd2452d1e53708019f7dbd9",
  "source_text_sha256": "10cb4109329cef5b1ccc26c0456d49d122c6a4e7cdd2452d1e53708019f7dbd9",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00baacb8",
        "00baadcb"
      ]
    ],
    "bytes_sha256": "6fc170fe1234708ea9b40deac9193262955c5e6ff8f0418514e465f890082e18",
    "instruction_count": 69,
    "instruction_bytes": 276,
    "body_bytes": 276,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c5db40](../00c5d/00c5db40.md)

## 呼び出し先

- [00c590f0](../00c59/00c590f0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2406 bytes

~~~c

long * _ZNKSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers8FieldDefEEENS_19__map_value_compareIS7_SB_NS_4lessIS7_EELb1EEENS5_ISB_EEE4findIS7_EENS_21__tree_const_iteratorISB_PNS_11__tree_nodeISB_PvEElEERKT_
                 (long param_1,byte *param_2)

{
  ulong uVar1;
  size_t sVar2;
  ulong uVar3;
  byte *__s2;
  byte bVar4;
  uint uVar5;
  int iVar6;
  void *pvVar7;
  long *plVar8;
  long *plVar9;
  long *plVar10;
  
  plVar8 = (long *)(param_1 + 8);
  plVar10 = (long *)*plVar8;
  if (plVar10 != (long *)0x0) {
    uVar3 = *(ulong *)(param_2 + 8);
    __s2 = *(byte **)(param_2 + 0x10);
    plVar9 = plVar8;
    if ((*param_2 & 1) == 0) {
      __s2 = param_2 + 1;
      uVar3 = (ulong)(*param_2 >> 1);
    }
    do {
      bVar4 = *(byte *)(plVar10 + 4);
      uVar1 = (ulong)(bVar4 >> 1);
      if ((bVar4 & 1) != 0) {
        uVar1 = plVar10[5];
      }
      sVar2 = uVar3;
      if (uVar1 <= uVar3) {
        sVar2 = uVar1;
      }
      if (sVar2 == 0) {
LAB_00baacf8:
        uVar5 = (uint)(uVar3 < uVar1);
        if (uVar1 < uVar3) {
          uVar5 = 0xffffffff;
        }
      }
      else {
        pvVar7 = (void *)plVar10[6];
        if ((bVar4 & 1) == 0) {
          pvVar7 = (void *)((long)plVar10 + 0x21);
        }
        uVar5 = memcmp(pvVar7,__s2,sVar2);
        if (uVar5 == 0) goto LAB_00baacf8;
      }
      if ((int)uVar5 >= 0) {
        plVar9 = plVar10;
      }
      plVar10 = (long *)plVar10[(int)uVar5 < 0];
    } while (plVar10 != (long *)0x0);
    if (plVar9 != plVar8) {
      bVar4 = *(byte *)(plVar9 + 4);
      uVar1 = (ulong)(bVar4 >> 1);
      if ((bVar4 & 1) != 0) {
        uVar1 = plVar9[5];
      }
      sVar2 = uVar1;
      if (uVar3 <= uVar1) {
        sVar2 = uVar3;
      }
      if (sVar2 != 0) {
        pvVar7 = (void *)plVar9[6];
                    /* try { // try from 00baad94 to 00caad9f has its CatchHandler @ 00bad07c */
        if ((bVar4 & 1) == 0) {
          pvVar7 = (void *)((long)plVar9 + 0x21);
        }
        iVar6 = memcmp(__s2,pvVar7,sVar2);
        if (iVar6 != 0) {
          if (iVar6 < 0) {
            return plVar8;
          }
          return plVar9;
        }
      }
      if (uVar1 <= uVar3) {
        return plVar9;
      }
    }
  }
                    /* try { // try from 00baadb8 to 00caadc3 has its CatchHandler @ 00bad06c */
  return plVar8;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00baacb8"></a> `00baacb8` | `f8 5f bc a9` | stp x24,x23,[sp, #-0x40]! | `FALL_THROUGH`
<a id="insn-00baacbc"></a> `00baacbc` | `f6 57 01 a9` | stp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00baacc0"></a> `00baacc0` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00baacc4"></a> `00baacc4` | `fd 7b 03 a9` | stp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00baacc8"></a> `00baacc8` | `fd c3 00 91` | add x29,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00baaccc"></a> `00baaccc` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00baacd0"></a> `00baacd0` | `77 8e 40 f8` | ldr x23,[x19, #0x8]! | `FALL_THROUGH`
<a id="insn-00baacd4"></a> `00baacd4` | `f7 06 00 b4` | cbz x23,0x00baadb0 | `CONDITIONAL_JUMP`
<a id="insn-00baacd8"></a> `00baacd8` | `28 00 40 39` | ldrb w8,[x1] | `FALL_THROUGH`
<a id="insn-00baacdc"></a> `00baacdc` | `29 a8 40 a9` | ldp x9,x10,[x1, #0x8] | `FALL_THROUGH`
<a id="insn-00baace0"></a> `00baace0` | `f4 03 13 aa` | mov x20,x19 | `FALL_THROUGH`
<a id="insn-00baace4"></a> `00baace4` | `0b fd 41 d3` | lsr x11,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00baace8"></a> `00baace8` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00baacec"></a> `00baacec` | `76 01 89 9a` | csel x22,x11,x9,eq | `FALL_THROUGH`
<a id="insn-00baacf0"></a> `00baacf0` | `55 15 81 9a` | csinc x21,x10,x1,ne | `FALL_THROUGH`
<a id="insn-00baacf4"></a> `00baacf4` | `0a 00 00 14` | b 0x00baad1c | `UNCONDITIONAL_JUMP`
<a id="insn-00baacf8"></a> `00baacf8` | `df 02 18 eb` | cmp x22,x24 | `FALL_THROUGH`
<a id="insn-00baacfc"></a> `00baacfc` | `e8 27 9f 1a` | cset w8,cc | `FALL_THROUGH`
<a id="insn-00baad00"></a> `00baad00` | `1f 03 16 eb` | cmp x24,x22 | `FALL_THROUGH`
<a id="insn-00baad04"></a> `00baad04` | `00 21 9f 5a` | csinv w0,w8,wzr,cs | `FALL_THROUGH`
<a id="insn-00baad08"></a> `00baad08` | `1f 00 00 71` | cmp w0,#0x0 | `FALL_THROUGH`
<a id="insn-00baad0c"></a> `00baad0c` | `e8 a7 9f 1a` | cset w8,lt | `FALL_THROUGH`
<a id="insn-00baad10"></a> `00baad10` | `94 b2 97 9a` | csel x20,x20,x23,lt | `FALL_THROUGH`
<a id="insn-00baad14"></a> `00baad14` | `f7 5a 68 f8` | ldr x23,[x23, w8, UXTW #0x3] | `FALL_THROUGH`
<a id="insn-00baad18"></a> `00baad18` | `37 02 00 b4` | cbz x23,0x00baad5c | `CONDITIONAL_JUMP`
<a id="insn-00baad1c"></a> `00baad1c` | `e8 03 17 aa` | mov x8,x23 | `FALL_THROUGH`
<a id="insn-00baad20"></a> `00baad20` | `09 0d 42 38` | ldrb w9,[x8, #0x20]! | `FALL_THROUGH`
<a id="insn-00baad24"></a> `00baad24` | `0a 05 40 f9` | ldr x10,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00baad28"></a> `00baad28` | `2b fd 41 d3` | lsr x11,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00baad2c"></a> `00baad2c` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00baad30"></a> `00baad30` | `78 01 8a 9a` | csel x24,x11,x10,eq | `FALL_THROUGH`
<a id="insn-00baad34"></a> `00baad34` | `df 02 18 eb` | cmp x22,x24 | `FALL_THROUGH`
<a id="insn-00baad38"></a> `00baad38` | `c2 32 98 9a` | csel x2,x22,x24,cc | `FALL_THROUGH`
<a id="insn-00baad3c"></a> `00baad3c` | `e2 fd ff b4` | cbz x2,0x00baacf8 | `CONDITIONAL_JUMP`
<a id="insn-00baad40"></a> `00baad40` | `ea 1a 40 f9` | ldr x10,[x23, #0x30] | `FALL_THROUGH`
<a id="insn-00baad44"></a> `00baad44` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00baad48"></a> `00baad48` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00baad4c"></a> `00baad4c` | `40 15 88 9a` | csinc x0,x10,x8,ne | `FALL_THROUGH`
<a id="insn-00baad50"></a> `00baad50` | `e8 b8 02 94` | bl 0x00c590f0 | `UNCONDITIONAL_CALL`
<a id="insn-00baad54"></a> `00baad54` | `a0 fd ff 35` | cbnz w0,0x00baad08 | `CONDITIONAL_JUMP`
<a id="insn-00baad58"></a> `00baad58` | `e8 ff ff 17` | b 0x00baacf8 | `UNCONDITIONAL_JUMP`
<a id="insn-00baad5c"></a> `00baad5c` | `9f 02 13 eb` | cmp x20,x19 | `FALL_THROUGH`
<a id="insn-00baad60"></a> `00baad60` | `80 02 00 54` | b.eq 0x00baadb0 | `CONDITIONAL_JUMP`
<a id="insn-00baad64"></a> `00baad64` | `e8 03 14 aa` | mov x8,x20 | `FALL_THROUGH`
<a id="insn-00baad68"></a> `00baad68` | `09 0d 42 38` | ldrb w9,[x8, #0x20]! | `FALL_THROUGH`
<a id="insn-00baad6c"></a> `00baad6c` | `0a 05 40 f9` | ldr x10,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00baad70"></a> `00baad70` | `2b fd 41 d3` | lsr x11,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00baad74"></a> `00baad74` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00baad78"></a> `00baad78` | `77 01 8a 9a` | csel x23,x11,x10,eq | `FALL_THROUGH`
<a id="insn-00baad7c"></a> `00baad7c` | `ff 02 16 eb` | cmp x23,x22 | `FALL_THROUGH`
<a id="insn-00baad80"></a> `00baad80` | `e2 32 96 9a` | csel x2,x23,x22,cc | `FALL_THROUGH`
<a id="insn-00baad84"></a> `00baad84` | `22 01 00 b4` | cbz x2,0x00baada8 | `CONDITIONAL_JUMP`
<a id="insn-00baad88"></a> `00baad88` | `8a 1a 40 f9` | ldr x10,[x20, #0x30] | `FALL_THROUGH`
<a id="insn-00baad8c"></a> `00baad8c` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00baad90"></a> `00baad90` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00baad94"></a> `00baad94` | `41 15 88 9a` | csinc x1,x10,x8,ne | `FALL_THROUGH`
<a id="insn-00baad98"></a> `00baad98` | `d6 b8 02 94` | bl 0x00c590f0 | `UNCONDITIONAL_CALL`
<a id="insn-00baad9c"></a> `00baad9c` | `60 00 00 34` | cbz w0,0x00baada8 | `CONDITIONAL_JUMP`
<a id="insn-00baada0"></a> `00baada0` | `80 00 f8 37` | tbnz w0,#0x1f,0x00baadb0 | `CONDITIONAL_JUMP`
<a id="insn-00baada4"></a> `00baada4` | `04 00 00 14` | b 0x00baadb4 | `UNCONDITIONAL_JUMP`
<a id="insn-00baada8"></a> `00baada8` | `df 02 17 eb` | cmp x22,x23 | `FALL_THROUGH`
<a id="insn-00baadac"></a> `00baadac` | `42 00 00 54` | b.cs 0x00baadb4 | `CONDITIONAL_JUMP`
<a id="insn-00baadb0"></a> `00baadb0` | `f4 03 13 aa` | mov x20,x19 | `FALL_THROUGH`
<a id="insn-00baadb4"></a> `00baadb4` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00baadb8"></a> `00baadb8` | `fd 7b 43 a9` | ldp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00baadbc"></a> `00baadbc` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00baadc0"></a> `00baadc0` | `f6 57 41 a9` | ldp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00baadc4"></a> `00baadc4` | `f8 5f c4 a8` | ldp x24,x23,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-00baadc8"></a> `00baadc8` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00baacb8`](#insn-00baacb8) 範囲 `[['00baacb8', '00baacd7']]`
  - `CONDITIONAL_JUMP` [`00baacd4`](#insn-00baacd4) → [`00baadb0`](#insn-00baadb0)
  - `FALL_THROUGH` [`00baacd4`](#insn-00baacd4) → [`00baacd8`](#insn-00baacd8)
- ブロック [`00baacd8`](#insn-00baacd8) 範囲 `[['00baacd8', '00baacf7']]`
  - `UNCONDITIONAL_JUMP` [`00baacf4`](#insn-00baacf4) → [`00baad1c`](#insn-00baad1c)
- ブロック [`00baacf8`](#insn-00baacf8) 範囲 `[['00baacf8', '00baad07']]`
  - `FALL_THROUGH` [`00baad04`](#insn-00baad04) → [`00baad08`](#insn-00baad08)
- ブロック [`00baad08`](#insn-00baad08) 範囲 `[['00baad08', '00baad1b']]`
  - `CONDITIONAL_JUMP` [`00baad18`](#insn-00baad18) → [`00baad5c`](#insn-00baad5c)
  - `FALL_THROUGH` [`00baad18`](#insn-00baad18) → [`00baad1c`](#insn-00baad1c)
- ブロック [`00baad1c`](#insn-00baad1c) 範囲 `[['00baad1c', '00baad3f']]`
  - `CONDITIONAL_JUMP` [`00baad3c`](#insn-00baad3c) → [`00baacf8`](#insn-00baacf8)
  - `FALL_THROUGH` [`00baad3c`](#insn-00baad3c) → [`00baad40`](#insn-00baad40)
- ブロック [`00baad40`](#insn-00baad40) 範囲 `[['00baad40', '00baad57']]`
  - `CONDITIONAL_JUMP` [`00baad54`](#insn-00baad54) → [`00baad08`](#insn-00baad08)
  - `FALL_THROUGH` [`00baad54`](#insn-00baad54) → [`00baad58`](#insn-00baad58)
- ブロック [`00baad58`](#insn-00baad58) 範囲 `[['00baad58', '00baad5b']]`
  - `UNCONDITIONAL_JUMP` [`00baad58`](#insn-00baad58) → [`00baacf8`](#insn-00baacf8)
- ブロック [`00baad5c`](#insn-00baad5c) 範囲 `[['00baad5c', '00baad63']]`
  - `CONDITIONAL_JUMP` [`00baad60`](#insn-00baad60) → [`00baadb0`](#insn-00baadb0)
  - `FALL_THROUGH` [`00baad60`](#insn-00baad60) → [`00baad64`](#insn-00baad64)
- ブロック [`00baad64`](#insn-00baad64) 範囲 `[['00baad64', '00baad87']]`
  - `CONDITIONAL_JUMP` [`00baad84`](#insn-00baad84) → [`00baada8`](#insn-00baada8)
  - `FALL_THROUGH` [`00baad84`](#insn-00baad84) → [`00baad88`](#insn-00baad88)
- ブロック [`00baad88`](#insn-00baad88) 範囲 `[['00baad88', '00baad93']]`
  - `FALL_THROUGH` [`00baad90`](#insn-00baad90) → [`00baad94`](#insn-00baad94)
- ブロック [`00baad94`](#insn-00baad94) 範囲 `[['00baad94', '00baad9f']]`
  - `CONDITIONAL_JUMP` [`00baad9c`](#insn-00baad9c) → [`00baada8`](#insn-00baada8)
  - `FALL_THROUGH` [`00baad9c`](#insn-00baad9c) → [`00baada0`](#insn-00baada0)
- ブロック [`00baada0`](#insn-00baada0) 範囲 `[['00baada0', '00baada3']]`
  - `CONDITIONAL_JUMP` [`00baada0`](#insn-00baada0) → [`00baadb0`](#insn-00baadb0)
  - `FALL_THROUGH` [`00baada0`](#insn-00baada0) → [`00baada4`](#insn-00baada4)
- ブロック [`00baada4`](#insn-00baada4) 範囲 `[['00baada4', '00baada7']]`
  - `UNCONDITIONAL_JUMP` [`00baada4`](#insn-00baada4) → [`00baadb4`](#insn-00baadb4)
- ブロック [`00baada8`](#insn-00baada8) 範囲 `[['00baada8', '00baadaf']]`
  - `CONDITIONAL_JUMP` [`00baadac`](#insn-00baadac) → [`00baadb4`](#insn-00baadb4)
  - `FALL_THROUGH` [`00baadac`](#insn-00baadac) → [`00baadb0`](#insn-00baadb0)
- ブロック [`00baadb0`](#insn-00baadb0) 範囲 `[['00baadb0', '00baadb3']]`
  - `FALL_THROUGH` [`00baadb0`](#insn-00baadb0) → [`00baadb4`](#insn-00baadb4)
- ブロック [`00baadb4`](#insn-00baadb4) 範囲 `[['00baadb4', '00baadb7']]`
  - `FALL_THROUGH` [`00baadb4`](#insn-00baadb4) → [`00baadb8`](#insn-00baadb8)
- ブロック [`00baadb8`](#insn-00baadb8) 範囲 `[['00baadb8', '00baadcb']]`

## 命令位置別の参照

- [`00baacb8`](#insn-00baacb8) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baacbc`](#insn-00baacbc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baacc0`](#insn-00baacc0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baacc4`](#insn-00baacc4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baacd4`](#insn-00baacd4) → [`00baadb0`](#insn-00baadb0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baacf4`](#insn-00baacf4) → [`00baad1c`](#insn-00baad1c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baad18`](#insn-00baad18) → [`00baad5c`](#insn-00baad5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baad3c`](#insn-00baad3c) → [`00baacf8`](#insn-00baacf8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baad50`](#insn-00baad50) → [`00c590f0`](../00c59/00c590f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c590f0` · 推定シンボル `None` · 推定型 `None`
- [`00baad54`](#insn-00baad54) → [`00baad08`](#insn-00baad08) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baad58`](#insn-00baad58) → [`00baacf8`](#insn-00baacf8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baad60`](#insn-00baad60) → [`00baadb0`](#insn-00baadb0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baad84`](#insn-00baad84) → [`00baada8`](#insn-00baada8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baad98`](#insn-00baad98) → [`00c590f0`](../00c59/00c590f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c590f0` · 推定シンボル `None` · 推定型 `None`
- [`00baad9c`](#insn-00baad9c) → [`00baada8`](#insn-00baada8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baada0`](#insn-00baada0) → [`00baadb0`](#insn-00baadb0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baada4`](#insn-00baada4) → [`00baadb4`](#insn-00baadb4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baadac`](#insn-00baadac) → [`00baadb4`](#insn-00baadb4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baadb8`](#insn-00baadb8) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baadbc`](#insn-00baadbc) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baadc0`](#insn-00baadc0) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00baacb8`](#insn-00baacb8)

~~~json
{
  "source": "00baacb8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baacbc`](#insn-00baacbc)

~~~json
{
  "source": "00baacbc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baacc0`](#insn-00baacc0)

~~~json
{
  "source": "00baacc0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baacc4`](#insn-00baacc4)

~~~json
{
  "source": "00baacc4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baacd4`](#insn-00baacd4)

~~~json
{
  "source": "00baacd4",
  "target": "00baadb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baacf4`](#insn-00baacf4)

~~~json
{
  "source": "00baacf4",
  "target": "00baad1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baad18`](#insn-00baad18)

~~~json
{
  "source": "00baad18",
  "target": "00baad5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baad3c`](#insn-00baad3c)

~~~json
{
  "source": "00baad3c",
  "target": "00baacf8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baad50`](#insn-00baad50)

~~~json
{
  "source": "00baad50",
  "target": "00c590f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baad54`](#insn-00baad54)

~~~json
{
  "source": "00baad54",
  "target": "00baad08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baad58`](#insn-00baad58)

~~~json
{
  "source": "00baad58",
  "target": "00baacf8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baad60`](#insn-00baad60)

~~~json
{
  "source": "00baad60",
  "target": "00baadb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baad84`](#insn-00baad84)

~~~json
{
  "source": "00baad84",
  "target": "00baada8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baad98`](#insn-00baad98)

~~~json
{
  "source": "00baad98",
  "target": "00c590f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baad9c`](#insn-00baad9c)

~~~json
{
  "source": "00baad9c",
  "target": "00baada8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baada0`](#insn-00baada0)

~~~json
{
  "source": "00baada0",
  "target": "00baadb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baada4`](#insn-00baada4)

~~~json
{
  "source": "00baada4",
  "target": "00baadb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baadac`](#insn-00baadac)

~~~json
{
  "source": "00baadac",
  "target": "00baadb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baadb8`](#insn-00baadb8)

~~~json
{
  "source": "00baadb8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baadbc`](#insn-00baadbc)

~~~json
{
  "source": "00baadbc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baadc0`](#insn-00baadc0)

~~~json
{
  "source": "00baadc0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
