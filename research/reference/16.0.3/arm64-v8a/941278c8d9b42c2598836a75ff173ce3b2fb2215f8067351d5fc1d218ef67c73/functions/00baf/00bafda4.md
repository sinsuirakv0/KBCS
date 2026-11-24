# 00bafda4

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00baedb0`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bae/00baedb0.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0035.md#compare-b16a36579a70997bfb9f13fe7181d885)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bafda4",
  "name": "_ZNKSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_3setIN11flatbuffers12IncludedFileENS_4lessISA_EENS5_ISA_EEEEEENS_19__map_value_compareIS7_SF_NSB_IS7_EELb1EEENS5_ISF_EEE4findIS7_EENS_21__tree_const_iteratorISF_PNS_11__tree_nodeISF_PvEElEERKT_",
  "size": 276,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "acddd6a0da8546efd43bc531b29d45e5f649300953e5e2b6edd9e1250a5b2380",
  "source_text_sha256": "acddd6a0da8546efd43bc531b29d45e5f649300953e5e2b6edd9e1250a5b2380",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bafda4",
        "00bafeb7"
      ]
    ],
    "bytes_sha256": "43ca25ea7eca9d00e9a4a04b8ce3854127ac909d6e3f0f5923f962ea884ff64d",
    "instruction_count": 69,
    "instruction_bytes": 276,
    "body_bytes": 276,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c5db00](../00c5d/00c5db00.md)

## 呼び出し先

- [00c590f0](../00c59/00c590f0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2246 bytes

~~~c

long * _ZNKSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_3setIN11flatbuffers12IncludedFileENS_4lessISA_EENS5_ISA_EEEEEENS_19__map_value_compareIS7_SF_NSB_IS7_EELb1EEENS5_ISF_EEE4findIS7_EENS_21__tree_const_iteratorISF_PNS_11__tree_nodeISF_PvEElEERKT_
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
LAB_00bafde4:
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
        if (uVar5 == 0) goto LAB_00bafde4;
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
  return plVar8;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bafda4"></a> `00bafda4` | `f8 5f bc a9` | stp x24,x23,[sp, #-0x40]! | `FALL_THROUGH`
<a id="insn-00bafda8"></a> `00bafda8` | `f6 57 01 a9` | stp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bafdac"></a> `00bafdac` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bafdb0"></a> `00bafdb0` | `fd 7b 03 a9` | stp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bafdb4"></a> `00bafdb4` | `fd c3 00 91` | add x29,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00bafdb8"></a> `00bafdb8` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bafdbc"></a> `00bafdbc` | `77 8e 40 f8` | ldr x23,[x19, #0x8]! | `FALL_THROUGH`
<a id="insn-00bafdc0"></a> `00bafdc0` | `f7 06 00 b4` | cbz x23,0x00bafe9c | `CONDITIONAL_JUMP`
<a id="insn-00bafdc4"></a> `00bafdc4` | `28 00 40 39` | ldrb w8,[x1] | `FALL_THROUGH`
<a id="insn-00bafdc8"></a> `00bafdc8` | `29 a8 40 a9` | ldp x9,x10,[x1, #0x8] | `FALL_THROUGH`
<a id="insn-00bafdcc"></a> `00bafdcc` | `f4 03 13 aa` | mov x20,x19 | `FALL_THROUGH`
<a id="insn-00bafdd0"></a> `00bafdd0` | `0b fd 41 d3` | lsr x11,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bafdd4"></a> `00bafdd4` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bafdd8"></a> `00bafdd8` | `76 01 89 9a` | csel x22,x11,x9,eq | `FALL_THROUGH`
<a id="insn-00bafddc"></a> `00bafddc` | `55 15 81 9a` | csinc x21,x10,x1,ne | `FALL_THROUGH`
<a id="insn-00bafde0"></a> `00bafde0` | `0a 00 00 14` | b 0x00bafe08 | `UNCONDITIONAL_JUMP`
<a id="insn-00bafde4"></a> `00bafde4` | `df 02 18 eb` | cmp x22,x24 | `FALL_THROUGH`
<a id="insn-00bafde8"></a> `00bafde8` | `e8 27 9f 1a` | cset w8,cc | `FALL_THROUGH`
<a id="insn-00bafdec"></a> `00bafdec` | `1f 03 16 eb` | cmp x24,x22 | `FALL_THROUGH`
<a id="insn-00bafdf0"></a> `00bafdf0` | `00 21 9f 5a` | csinv w0,w8,wzr,cs | `FALL_THROUGH`
<a id="insn-00bafdf4"></a> `00bafdf4` | `1f 00 00 71` | cmp w0,#0x0 | `FALL_THROUGH`
<a id="insn-00bafdf8"></a> `00bafdf8` | `e8 a7 9f 1a` | cset w8,lt | `FALL_THROUGH`
<a id="insn-00bafdfc"></a> `00bafdfc` | `94 b2 97 9a` | csel x20,x20,x23,lt | `FALL_THROUGH`
<a id="insn-00bafe00"></a> `00bafe00` | `f7 5a 68 f8` | ldr x23,[x23, w8, UXTW #0x3] | `FALL_THROUGH`
<a id="insn-00bafe04"></a> `00bafe04` | `37 02 00 b4` | cbz x23,0x00bafe48 | `CONDITIONAL_JUMP`
<a id="insn-00bafe08"></a> `00bafe08` | `e8 03 17 aa` | mov x8,x23 | `FALL_THROUGH`
<a id="insn-00bafe0c"></a> `00bafe0c` | `09 0d 42 38` | ldrb w9,[x8, #0x20]! | `FALL_THROUGH`
<a id="insn-00bafe10"></a> `00bafe10` | `0a 05 40 f9` | ldr x10,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00bafe14"></a> `00bafe14` | `2b fd 41 d3` | lsr x11,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bafe18"></a> `00bafe18` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00bafe1c"></a> `00bafe1c` | `78 01 8a 9a` | csel x24,x11,x10,eq | `FALL_THROUGH`
<a id="insn-00bafe20"></a> `00bafe20` | `df 02 18 eb` | cmp x22,x24 | `FALL_THROUGH`
<a id="insn-00bafe24"></a> `00bafe24` | `c2 32 98 9a` | csel x2,x22,x24,cc | `FALL_THROUGH`
<a id="insn-00bafe28"></a> `00bafe28` | `e2 fd ff b4` | cbz x2,0x00bafde4 | `CONDITIONAL_JUMP`
<a id="insn-00bafe2c"></a> `00bafe2c` | `ea 1a 40 f9` | ldr x10,[x23, #0x30] | `FALL_THROUGH`
<a id="insn-00bafe30"></a> `00bafe30` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00bafe34"></a> `00bafe34` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00bafe38"></a> `00bafe38` | `40 15 88 9a` | csinc x0,x10,x8,ne | `FALL_THROUGH`
<a id="insn-00bafe3c"></a> `00bafe3c` | `ad a4 02 94` | bl 0x00c590f0 | `UNCONDITIONAL_CALL`
<a id="insn-00bafe40"></a> `00bafe40` | `a0 fd ff 35` | cbnz w0,0x00bafdf4 | `CONDITIONAL_JUMP`
<a id="insn-00bafe44"></a> `00bafe44` | `e8 ff ff 17` | b 0x00bafde4 | `UNCONDITIONAL_JUMP`
<a id="insn-00bafe48"></a> `00bafe48` | `9f 02 13 eb` | cmp x20,x19 | `FALL_THROUGH`
<a id="insn-00bafe4c"></a> `00bafe4c` | `80 02 00 54` | b.eq 0x00bafe9c | `CONDITIONAL_JUMP`
<a id="insn-00bafe50"></a> `00bafe50` | `e8 03 14 aa` | mov x8,x20 | `FALL_THROUGH`
<a id="insn-00bafe54"></a> `00bafe54` | `09 0d 42 38` | ldrb w9,[x8, #0x20]! | `FALL_THROUGH`
<a id="insn-00bafe58"></a> `00bafe58` | `0a 05 40 f9` | ldr x10,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00bafe5c"></a> `00bafe5c` | `2b fd 41 d3` | lsr x11,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bafe60"></a> `00bafe60` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00bafe64"></a> `00bafe64` | `77 01 8a 9a` | csel x23,x11,x10,eq | `FALL_THROUGH`
<a id="insn-00bafe68"></a> `00bafe68` | `ff 02 16 eb` | cmp x23,x22 | `FALL_THROUGH`
<a id="insn-00bafe6c"></a> `00bafe6c` | `e2 32 96 9a` | csel x2,x23,x22,cc | `FALL_THROUGH`
<a id="insn-00bafe70"></a> `00bafe70` | `22 01 00 b4` | cbz x2,0x00bafe94 | `CONDITIONAL_JUMP`
<a id="insn-00bafe74"></a> `00bafe74` | `8a 1a 40 f9` | ldr x10,[x20, #0x30] | `FALL_THROUGH`
<a id="insn-00bafe78"></a> `00bafe78` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00bafe7c"></a> `00bafe7c` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bafe80"></a> `00bafe80` | `41 15 88 9a` | csinc x1,x10,x8,ne | `FALL_THROUGH`
<a id="insn-00bafe84"></a> `00bafe84` | `9b a4 02 94` | bl 0x00c590f0 | `UNCONDITIONAL_CALL`
<a id="insn-00bafe88"></a> `00bafe88` | `60 00 00 34` | cbz w0,0x00bafe94 | `CONDITIONAL_JUMP`
<a id="insn-00bafe8c"></a> `00bafe8c` | `80 00 f8 37` | tbnz w0,#0x1f,0x00bafe9c | `CONDITIONAL_JUMP`
<a id="insn-00bafe90"></a> `00bafe90` | `04 00 00 14` | b 0x00bafea0 | `UNCONDITIONAL_JUMP`
<a id="insn-00bafe94"></a> `00bafe94` | `df 02 17 eb` | cmp x22,x23 | `FALL_THROUGH`
<a id="insn-00bafe98"></a> `00bafe98` | `42 00 00 54` | b.cs 0x00bafea0 | `CONDITIONAL_JUMP`
<a id="insn-00bafe9c"></a> `00bafe9c` | `f4 03 13 aa` | mov x20,x19 | `FALL_THROUGH`
<a id="insn-00bafea0"></a> `00bafea0` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bafea4"></a> `00bafea4` | `fd 7b 43 a9` | ldp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bafea8"></a> `00bafea8` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bafeac"></a> `00bafeac` | `f6 57 41 a9` | ldp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bafeb0"></a> `00bafeb0` | `f8 5f c4 a8` | ldp x24,x23,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-00bafeb4"></a> `00bafeb4` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bafda4`](#insn-00bafda4) 範囲 `[['00bafda4', '00bafdc3']]`
  - `CONDITIONAL_JUMP` [`00bafdc0`](#insn-00bafdc0) → [`00bafe9c`](#insn-00bafe9c)
  - `FALL_THROUGH` [`00bafdc0`](#insn-00bafdc0) → [`00bafdc4`](#insn-00bafdc4)
- ブロック [`00bafdc4`](#insn-00bafdc4) 範囲 `[['00bafdc4', '00bafde3']]`
  - `UNCONDITIONAL_JUMP` [`00bafde0`](#insn-00bafde0) → [`00bafe08`](#insn-00bafe08)
- ブロック [`00bafde4`](#insn-00bafde4) 範囲 `[['00bafde4', '00bafdf3']]`
  - `FALL_THROUGH` [`00bafdf0`](#insn-00bafdf0) → [`00bafdf4`](#insn-00bafdf4)
- ブロック [`00bafdf4`](#insn-00bafdf4) 範囲 `[['00bafdf4', '00bafe07']]`
  - `CONDITIONAL_JUMP` [`00bafe04`](#insn-00bafe04) → [`00bafe48`](#insn-00bafe48)
  - `FALL_THROUGH` [`00bafe04`](#insn-00bafe04) → [`00bafe08`](#insn-00bafe08)
- ブロック [`00bafe08`](#insn-00bafe08) 範囲 `[['00bafe08', '00bafe2b']]`
  - `CONDITIONAL_JUMP` [`00bafe28`](#insn-00bafe28) → [`00bafde4`](#insn-00bafde4)
  - `FALL_THROUGH` [`00bafe28`](#insn-00bafe28) → [`00bafe2c`](#insn-00bafe2c)
- ブロック [`00bafe2c`](#insn-00bafe2c) 範囲 `[['00bafe2c', '00bafe43']]`
  - `CONDITIONAL_JUMP` [`00bafe40`](#insn-00bafe40) → [`00bafdf4`](#insn-00bafdf4)
  - `FALL_THROUGH` [`00bafe40`](#insn-00bafe40) → [`00bafe44`](#insn-00bafe44)
- ブロック [`00bafe44`](#insn-00bafe44) 範囲 `[['00bafe44', '00bafe47']]`
  - `UNCONDITIONAL_JUMP` [`00bafe44`](#insn-00bafe44) → [`00bafde4`](#insn-00bafde4)
- ブロック [`00bafe48`](#insn-00bafe48) 範囲 `[['00bafe48', '00bafe4f']]`
  - `CONDITIONAL_JUMP` [`00bafe4c`](#insn-00bafe4c) → [`00bafe9c`](#insn-00bafe9c)
  - `FALL_THROUGH` [`00bafe4c`](#insn-00bafe4c) → [`00bafe50`](#insn-00bafe50)
- ブロック [`00bafe50`](#insn-00bafe50) 範囲 `[['00bafe50', '00bafe73']]`
  - `CONDITIONAL_JUMP` [`00bafe70`](#insn-00bafe70) → [`00bafe94`](#insn-00bafe94)
  - `FALL_THROUGH` [`00bafe70`](#insn-00bafe70) → [`00bafe74`](#insn-00bafe74)
- ブロック [`00bafe74`](#insn-00bafe74) 範囲 `[['00bafe74', '00bafe8b']]`
  - `CONDITIONAL_JUMP` [`00bafe88`](#insn-00bafe88) → [`00bafe94`](#insn-00bafe94)
  - `FALL_THROUGH` [`00bafe88`](#insn-00bafe88) → [`00bafe8c`](#insn-00bafe8c)
- ブロック [`00bafe8c`](#insn-00bafe8c) 範囲 `[['00bafe8c', '00bafe8f']]`
  - `CONDITIONAL_JUMP` [`00bafe8c`](#insn-00bafe8c) → [`00bafe9c`](#insn-00bafe9c)
  - `FALL_THROUGH` [`00bafe8c`](#insn-00bafe8c) → [`00bafe90`](#insn-00bafe90)
- ブロック [`00bafe90`](#insn-00bafe90) 範囲 `[['00bafe90', '00bafe93']]`
  - `UNCONDITIONAL_JUMP` [`00bafe90`](#insn-00bafe90) → [`00bafea0`](#insn-00bafea0)
- ブロック [`00bafe94`](#insn-00bafe94) 範囲 `[['00bafe94', '00bafe9b']]`
  - `CONDITIONAL_JUMP` [`00bafe98`](#insn-00bafe98) → [`00bafea0`](#insn-00bafea0)
  - `FALL_THROUGH` [`00bafe98`](#insn-00bafe98) → [`00bafe9c`](#insn-00bafe9c)
- ブロック [`00bafe9c`](#insn-00bafe9c) 範囲 `[['00bafe9c', '00bafe9f']]`
  - `FALL_THROUGH` [`00bafe9c`](#insn-00bafe9c) → [`00bafea0`](#insn-00bafea0)
- ブロック [`00bafea0`](#insn-00bafea0) 範囲 `[['00bafea0', '00bafeb7']]`

## 命令位置別の参照

- [`00bafda4`](#insn-00bafda4) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafda8`](#insn-00bafda8) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafdac`](#insn-00bafdac) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafdb0`](#insn-00bafdb0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafdc0`](#insn-00bafdc0) → [`00bafe9c`](#insn-00bafe9c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafde0`](#insn-00bafde0) → [`00bafe08`](#insn-00bafe08) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafe04`](#insn-00bafe04) → [`00bafe48`](#insn-00bafe48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafe28`](#insn-00bafe28) → [`00bafde4`](#insn-00bafde4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafe3c`](#insn-00bafe3c) → [`00c590f0`](../00c59/00c590f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c590f0` · 推定シンボル `None` · 推定型 `None`
- [`00bafe40`](#insn-00bafe40) → [`00bafdf4`](#insn-00bafdf4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafe44`](#insn-00bafe44) → [`00bafde4`](#insn-00bafde4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafe4c`](#insn-00bafe4c) → [`00bafe9c`](#insn-00bafe9c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafe70`](#insn-00bafe70) → [`00bafe94`](#insn-00bafe94) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafe84`](#insn-00bafe84) → [`00c590f0`](../00c59/00c590f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c590f0` · 推定シンボル `None` · 推定型 `None`
- [`00bafe88`](#insn-00bafe88) → [`00bafe94`](#insn-00bafe94) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafe8c`](#insn-00bafe8c) → [`00bafe9c`](#insn-00bafe9c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafe90`](#insn-00bafe90) → [`00bafea0`](#insn-00bafea0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafe98`](#insn-00bafe98) → [`00bafea0`](#insn-00bafea0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafea4`](#insn-00bafea4) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafea8`](#insn-00bafea8) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafeac`](#insn-00bafeac) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bafda4`](#insn-00bafda4)

~~~json
{
  "source": "00bafda4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafda8`](#insn-00bafda8)

~~~json
{
  "source": "00bafda8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafdac`](#insn-00bafdac)

~~~json
{
  "source": "00bafdac",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafdb0`](#insn-00bafdb0)

~~~json
{
  "source": "00bafdb0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafdc0`](#insn-00bafdc0)

~~~json
{
  "source": "00bafdc0",
  "target": "00bafe9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafde0`](#insn-00bafde0)

~~~json
{
  "source": "00bafde0",
  "target": "00bafe08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafe04`](#insn-00bafe04)

~~~json
{
  "source": "00bafe04",
  "target": "00bafe48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafe28`](#insn-00bafe28)

~~~json
{
  "source": "00bafe28",
  "target": "00bafde4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafe3c`](#insn-00bafe3c)

~~~json
{
  "source": "00bafe3c",
  "target": "00c590f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bafe40`](#insn-00bafe40)

~~~json
{
  "source": "00bafe40",
  "target": "00bafdf4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafe44`](#insn-00bafe44)

~~~json
{
  "source": "00bafe44",
  "target": "00bafde4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafe4c`](#insn-00bafe4c)

~~~json
{
  "source": "00bafe4c",
  "target": "00bafe9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafe70`](#insn-00bafe70)

~~~json
{
  "source": "00bafe70",
  "target": "00bafe94",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafe84`](#insn-00bafe84)

~~~json
{
  "source": "00bafe84",
  "target": "00c590f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bafe88`](#insn-00bafe88)

~~~json
{
  "source": "00bafe88",
  "target": "00bafe94",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafe8c`](#insn-00bafe8c)

~~~json
{
  "source": "00bafe8c",
  "target": "00bafe9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafe90`](#insn-00bafe90)

~~~json
{
  "source": "00bafe90",
  "target": "00bafea0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafe98`](#insn-00bafe98)

~~~json
{
  "source": "00bafe98",
  "target": "00bafea0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafea4`](#insn-00bafea4)

~~~json
{
  "source": "00bafea4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafea8`](#insn-00bafea8)

~~~json
{
  "source": "00bafea8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafeac`](#insn-00bafeac)

~~~json
{
  "source": "00bafeac",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
