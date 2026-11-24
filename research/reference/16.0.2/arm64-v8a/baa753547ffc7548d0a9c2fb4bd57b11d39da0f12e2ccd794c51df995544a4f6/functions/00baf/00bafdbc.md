# 00bafdbc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bafd20`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00baf/00bafd20.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/alignment_unresolved-0010.md#compare-d58de96926f9c97735c3dca03bcaba61)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00bb0db0`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb0/00bb0db0.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0035.md#compare-883d59301c28bae9a8bffb7a33d0a37b)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bafdbc",
  "name": "_ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers7RPCCallEEENS_19__map_value_compareIS7_SB_NS_4lessIS7_EELb1EEENS5_ISB_EEE12__find_equalIS7_EERPNS_16__tree_node_baseIPvEERPNS_15__tree_end_nodeISM_EERKT_",
  "size": 288,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "69642e47fe1a23c013b160a6b14ed5095eda1bfeb8676d8ad7db48656b8c8431",
  "source_text_sha256": "69642e47fe1a23c013b160a6b14ed5095eda1bfeb8676d8ad7db48656b8c8431",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bafdbc",
        "00bafedb"
      ]
    ],
    "bytes_sha256": "722d427650e83d305bb38091c298b7230cac84d7470197c3c7643fa5bd2f2698",
    "instruction_count": 72,
    "instruction_bytes": 288,
    "body_bytes": 288,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c5cff0](../00c5c/00c5cff0.md)

## 呼び出し先

- [00c58120](../00c58/00c58120.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2290 bytes

~~~c

long * _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers7RPCCallEEENS_19__map_value_compareIS7_SB_NS_4lessIS7_EELb1EEENS5_ISB_EEE12__find_equalIS7_EERPNS_16__tree_node_baseIPvEERPNS_15__tree_end_nodeISM_EERKT_
                 (long param_1,undefined8 *param_2,byte *param_3)

{
  ulong uVar1;
  size_t __n;
  void *__s2;
  ulong uVar2;
  byte *__s1;
  byte bVar3;
  int iVar4;
  long *plVar5;
  long *plVar6;
  long *plVar7;
  void *__s1_00;
  
  plVar5 = (long *)(param_1 + 8);
  plVar6 = (long *)*plVar5;
  if (plVar6 == (long *)0x0) {
    *param_2 = plVar5;
                    /* try { // try from 00bafec8 to 00caff7f has its CatchHandler @ 00bafaa4 */
    return plVar5;
  }
  uVar2 = *(ulong *)(param_3 + 8);
  __s1 = *(byte **)(param_3 + 0x10);
  plVar5 = (long *)(param_1 + 8);
  if ((*param_3 & 1) == 0) {
    __s1 = param_3 + 1;
    uVar2 = (ulong)(*param_3 >> 1);
  }
  do {
    while( true ) {
      plVar7 = plVar6;
      bVar3 = *(byte *)(plVar7 + 4);
      uVar1 = (ulong)(bVar3 >> 1);
      if ((bVar3 & 1) != 0) {
        uVar1 = plVar7[5];
      }
      __n = uVar1;
      if (uVar2 <= uVar1) {
        __n = uVar2;
      }
      if (__n == 0) break;
      __s1_00 = (void *)plVar7[6];
      __s2 = __s1_00;
      if ((bVar3 & 1) == 0) {
        __s2 = (void *)((long)plVar7 + 0x21);
      }
      iVar4 = memcmp(__s1,__s2,__n);
      if (iVar4 == 0) break;
      if (iVar4 < 0) goto LAB_00bafe70;
LAB_00bafe88:
      if ((bVar3 & 1) == 0) {
        __s1_00 = (void *)((long)plVar7 + 0x21);
      }
      iVar4 = memcmp(__s1_00,__s1,__n);
      if (iVar4 == 0) goto LAB_00bafe08;
      if (-1 < iVar4) goto LAB_00bafea4;
LAB_00bafe10:
      plVar5 = plVar7 + 1;
      plVar6 = (long *)*plVar5;
      if ((long *)*plVar5 == (long *)0x0) {
LAB_00bafea4:
        *param_2 = plVar7;
        return plVar5;
      }
    }
    if (uVar1 <= uVar2) {
      if (__n != 0) {
        __s1_00 = (void *)plVar7[6];
        goto LAB_00bafe88;
      }
LAB_00bafe08:
      if (uVar2 <= uVar1) goto LAB_00bafea4;
      goto LAB_00bafe10;
    }
LAB_00bafe70:
    plVar5 = plVar7;
    plVar6 = (long *)*plVar7;
    if ((long *)*plVar7 == (long *)0x0) {
      *param_2 = plVar7;
      return plVar7;
    }
  } while( true );
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bafdbc"></a> `00bafdbc` | `fc 6f ba a9` | stp x28,x27,[sp, #-0x60]! | `FALL_THROUGH`
<a id="insn-00bafdc0"></a> `00bafdc0` | `fa 67 01 a9` | stp x26,x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bafdc4"></a> `00bafdc4` | `f8 5f 02 a9` | stp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bafdc8"></a> `00bafdc8` | `f6 57 03 a9` | stp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bafdcc"></a> `00bafdcc` | `f4 4f 04 a9` | stp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bafdd0"></a> `00bafdd0` | `fd 7b 05 a9` | stp x29,x30,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bafdd4"></a> `00bafdd4` | `fd 43 01 91` | add x29,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00bafdd8"></a> `00bafdd8` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bafddc"></a> `00bafddc` | `97 8e 40 f8` | ldr x23,[x20, #0x8]! | `FALL_THROUGH`
<a id="insn-00bafde0"></a> `00bafde0` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00bafde4"></a> `00bafde4` | `57 06 00 b4` | cbz x23,0x00bafeac | `CONDITIONAL_JUMP`
<a id="insn-00bafde8"></a> `00bafde8` | `48 00 40 39` | ldrb w8,[x2] | `FALL_THROUGH`
<a id="insn-00bafdec"></a> `00bafdec` | `49 a8 40 a9` | ldp x9,x10,[x2, #0x8] | `FALL_THROUGH`
<a id="insn-00bafdf0"></a> `00bafdf0` | `14 20 00 91` | add x20,x0,#0x8 | `FALL_THROUGH`
<a id="insn-00bafdf4"></a> `00bafdf4` | `0b fd 41 d3` | lsr x11,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bafdf8"></a> `00bafdf8` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bafdfc"></a> `00bafdfc` | `78 01 89 9a` | csel x24,x11,x9,eq | `FALL_THROUGH`
<a id="insn-00bafe00"></a> `00bafe00` | `55 15 82 9a` | csinc x21,x10,x2,ne | `FALL_THROUGH`
<a id="insn-00bafe04"></a> `00bafe04` | `07 00 00 14` | b 0x00bafe20 | `UNCONDITIONAL_JUMP`
<a id="insn-00bafe08"></a> `00bafe08` | `3f 03 18 eb` | cmp x25,x24 | `FALL_THROUGH`
<a id="insn-00bafe0c"></a> `00bafe0c` | `c2 04 00 54` | b.cs 0x00bafea4 | `CONDITIONAL_JUMP`
<a id="insn-00bafe10"></a> `00bafe10` | `f4 03 17 aa` | mov x20,x23 | `FALL_THROUGH`
<a id="insn-00bafe14"></a> `00bafe14` | `88 8e 40 f8` | ldr x8,[x20, #0x8]! | `FALL_THROUGH`
<a id="insn-00bafe18"></a> `00bafe18` | `68 04 00 b4` | cbz x8,0x00bafea4 | `CONDITIONAL_JUMP`
<a id="insn-00bafe1c"></a> `00bafe1c` | `f7 03 08 aa` | mov x23,x8 | `FALL_THROUGH`
<a id="insn-00bafe20"></a> `00bafe20` | `fa 03 17 aa` | mov x26,x23 | `FALL_THROUGH`
<a id="insn-00bafe24"></a> `00bafe24` | `5b 0f 42 38` | ldrb w27,[x26, #0x20]! | `FALL_THROUGH`
<a id="insn-00bafe28"></a> `00bafe28` | `48 07 40 f9` | ldr x8,[x26, #0x8] | `FALL_THROUGH`
<a id="insn-00bafe2c"></a> `00bafe2c` | `69 ff 41 d3` | lsr x9,x27,#0x1 | `FALL_THROUGH`
<a id="insn-00bafe30"></a> `00bafe30` | `7f 03 00 72` | tst w27,#0x1 | `FALL_THROUGH`
<a id="insn-00bafe34"></a> `00bafe34` | `39 01 88 9a` | csel x25,x9,x8,eq | `FALL_THROUGH`
<a id="insn-00bafe38"></a> `00bafe38` | `3f 03 18 eb` | cmp x25,x24 | `FALL_THROUGH`
<a id="insn-00bafe3c"></a> `00bafe3c` | `36 33 98 9a` | csel x22,x25,x24,cc | `FALL_THROUGH`
<a id="insn-00bafe40"></a> `00bafe40` | `56 01 00 b4` | cbz x22,0x00bafe68 | `CONDITIONAL_JUMP`
<a id="insn-00bafe44"></a> `00bafe44` | `fc 1a 40 f9` | ldr x28,[x23, #0x30] | `FALL_THROUGH`
<a id="insn-00bafe48"></a> `00bafe48` | `7f 03 00 72` | tst w27,#0x1 | `FALL_THROUGH`
<a id="insn-00bafe4c"></a> `00bafe4c` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bafe50"></a> `00bafe50` | `e2 03 16 aa` | mov x2,x22 | `FALL_THROUGH`
<a id="insn-00bafe54"></a> `00bafe54` | `81 17 9a 9a` | csinc x1,x28,x26,ne | `FALL_THROUGH`
<a id="insn-00bafe58"></a> `00bafe58` | `b2 a0 02 94` | bl 0x00c58120 | `UNCONDITIONAL_CALL`
<a id="insn-00bafe5c"></a> `00bafe5c` | `60 00 00 34` | cbz w0,0x00bafe68 | `CONDITIONAL_JUMP`
<a id="insn-00bafe60"></a> `00bafe60` | `80 00 f8 37` | tbnz w0,#0x1f,0x00bafe70 | `CONDITIONAL_JUMP`
<a id="insn-00bafe64"></a> `00bafe64` | `09 00 00 14` | b 0x00bafe88 | `UNCONDITIONAL_JUMP`
<a id="insn-00bafe68"></a> `00bafe68` | `1f 03 19 eb` | cmp x24,x25 | `FALL_THROUGH`
<a id="insn-00bafe6c"></a> `00bafe6c` | `a2 00 00 54` | b.cs 0x00bafe80 | `CONDITIONAL_JUMP`
<a id="insn-00bafe70"></a> `00bafe70` | `e8 02 40 f9` | ldr x8,[x23] | `FALL_THROUGH`
<a id="insn-00bafe74"></a> `00bafe74` | `08 02 00 b4` | cbz x8,0x00bafeb4 | `CONDITIONAL_JUMP`
<a id="insn-00bafe78"></a> `00bafe78` | `f4 03 17 aa` | mov x20,x23 | `FALL_THROUGH`
<a id="insn-00bafe7c"></a> `00bafe7c` | `e8 ff ff 17` | b 0x00bafe1c | `UNCONDITIONAL_JUMP`
<a id="insn-00bafe80"></a> `00bafe80` | `56 fc ff b4` | cbz x22,0x00bafe08 | `CONDITIONAL_JUMP`
<a id="insn-00bafe84"></a> `00bafe84` | `fc 1a 40 f9` | ldr x28,[x23, #0x30] | `FALL_THROUGH`
<a id="insn-00bafe88"></a> `00bafe88` | `7f 03 00 72` | tst w27,#0x1 | `FALL_THROUGH`
<a id="insn-00bafe8c"></a> `00bafe8c` | `80 17 9a 9a` | csinc x0,x28,x26,ne | `FALL_THROUGH`
<a id="insn-00bafe90"></a> `00bafe90` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00bafe94"></a> `00bafe94` | `e2 03 16 aa` | mov x2,x22 | `FALL_THROUGH`
<a id="insn-00bafe98"></a> `00bafe98` | `a2 a0 02 94` | bl 0x00c58120 | `UNCONDITIONAL_CALL`
<a id="insn-00bafe9c"></a> `00bafe9c` | `60 fb ff 34` | cbz w0,0x00bafe08 | `CONDITIONAL_JUMP`
<a id="insn-00bafea0"></a> `00bafea0` | `80 fb ff 37` | tbnz w0,#0x1f,0x00bafe10 | `CONDITIONAL_JUMP`
<a id="insn-00bafea4"></a> `00bafea4` | `77 02 00 f9` | str x23,[x19] | `FALL_THROUGH`
<a id="insn-00bafea8"></a> `00bafea8` | `05 00 00 14` | b 0x00bafebc | `UNCONDITIONAL_JUMP`
<a id="insn-00bafeac"></a> `00bafeac` | `74 02 00 f9` | str x20,[x19] | `FALL_THROUGH`
<a id="insn-00bafeb0"></a> `00bafeb0` | `03 00 00 14` | b 0x00bafebc | `UNCONDITIONAL_JUMP`
<a id="insn-00bafeb4"></a> `00bafeb4` | `77 02 00 f9` | str x23,[x19] | `FALL_THROUGH`
<a id="insn-00bafeb8"></a> `00bafeb8` | `f4 03 17 aa` | mov x20,x23 | `FALL_THROUGH`
<a id="insn-00bafebc"></a> `00bafebc` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bafec0"></a> `00bafec0` | `fd 7b 45 a9` | ldp x29,x30,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bafec4"></a> `00bafec4` | `f4 4f 44 a9` | ldp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bafec8"></a> `00bafec8` | `f6 57 43 a9` | ldp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bafecc"></a> `00bafecc` | `f8 5f 42 a9` | ldp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bafed0"></a> `00bafed0` | `fa 67 41 a9` | ldp x26,x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bafed4"></a> `00bafed4` | `fc 6f c6 a8` | ldp x28,x27,[sp], #0x60 | `FALL_THROUGH`
<a id="insn-00bafed8"></a> `00bafed8` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bafdbc`](#insn-00bafdbc) 範囲 `[['00bafdbc', '00bafde7']]`
  - `CONDITIONAL_JUMP` [`00bafde4`](#insn-00bafde4) → [`00bafeac`](#insn-00bafeac)
  - `FALL_THROUGH` [`00bafde4`](#insn-00bafde4) → [`00bafde8`](#insn-00bafde8)
- ブロック [`00bafde8`](#insn-00bafde8) 範囲 `[['00bafde8', '00bafe07']]`
  - `UNCONDITIONAL_JUMP` [`00bafe04`](#insn-00bafe04) → [`00bafe20`](#insn-00bafe20)
- ブロック [`00bafe08`](#insn-00bafe08) 範囲 `[['00bafe08', '00bafe0f']]`
  - `CONDITIONAL_JUMP` [`00bafe0c`](#insn-00bafe0c) → [`00bafea4`](#insn-00bafea4)
  - `FALL_THROUGH` [`00bafe0c`](#insn-00bafe0c) → [`00bafe10`](#insn-00bafe10)
- ブロック [`00bafe10`](#insn-00bafe10) 範囲 `[['00bafe10', '00bafe1b']]`
  - `CONDITIONAL_JUMP` [`00bafe18`](#insn-00bafe18) → [`00bafea4`](#insn-00bafea4)
  - `FALL_THROUGH` [`00bafe18`](#insn-00bafe18) → [`00bafe1c`](#insn-00bafe1c)
- ブロック [`00bafe1c`](#insn-00bafe1c) 範囲 `[['00bafe1c', '00bafe1f']]`
  - `FALL_THROUGH` [`00bafe1c`](#insn-00bafe1c) → [`00bafe20`](#insn-00bafe20)
- ブロック [`00bafe20`](#insn-00bafe20) 範囲 `[['00bafe20', '00bafe43']]`
  - `CONDITIONAL_JUMP` [`00bafe40`](#insn-00bafe40) → [`00bafe68`](#insn-00bafe68)
  - `FALL_THROUGH` [`00bafe40`](#insn-00bafe40) → [`00bafe44`](#insn-00bafe44)
- ブロック [`00bafe44`](#insn-00bafe44) 範囲 `[['00bafe44', '00bafe5f']]`
  - `CONDITIONAL_JUMP` [`00bafe5c`](#insn-00bafe5c) → [`00bafe68`](#insn-00bafe68)
  - `FALL_THROUGH` [`00bafe5c`](#insn-00bafe5c) → [`00bafe60`](#insn-00bafe60)
- ブロック [`00bafe60`](#insn-00bafe60) 範囲 `[['00bafe60', '00bafe63']]`
  - `CONDITIONAL_JUMP` [`00bafe60`](#insn-00bafe60) → [`00bafe70`](#insn-00bafe70)
  - `FALL_THROUGH` [`00bafe60`](#insn-00bafe60) → [`00bafe64`](#insn-00bafe64)
- ブロック [`00bafe64`](#insn-00bafe64) 範囲 `[['00bafe64', '00bafe67']]`
  - `UNCONDITIONAL_JUMP` [`00bafe64`](#insn-00bafe64) → [`00bafe88`](#insn-00bafe88)
- ブロック [`00bafe68`](#insn-00bafe68) 範囲 `[['00bafe68', '00bafe6f']]`
  - `CONDITIONAL_JUMP` [`00bafe6c`](#insn-00bafe6c) → [`00bafe80`](#insn-00bafe80)
  - `FALL_THROUGH` [`00bafe6c`](#insn-00bafe6c) → [`00bafe70`](#insn-00bafe70)
- ブロック [`00bafe70`](#insn-00bafe70) 範囲 `[['00bafe70', '00bafe77']]`
  - `CONDITIONAL_JUMP` [`00bafe74`](#insn-00bafe74) → [`00bafeb4`](#insn-00bafeb4)
  - `FALL_THROUGH` [`00bafe74`](#insn-00bafe74) → [`00bafe78`](#insn-00bafe78)
- ブロック [`00bafe78`](#insn-00bafe78) 範囲 `[['00bafe78', '00bafe7f']]`
  - `UNCONDITIONAL_JUMP` [`00bafe7c`](#insn-00bafe7c) → [`00bafe1c`](#insn-00bafe1c)
- ブロック [`00bafe80`](#insn-00bafe80) 範囲 `[['00bafe80', '00bafe83']]`
  - `CONDITIONAL_JUMP` [`00bafe80`](#insn-00bafe80) → [`00bafe08`](#insn-00bafe08)
  - `FALL_THROUGH` [`00bafe80`](#insn-00bafe80) → [`00bafe84`](#insn-00bafe84)
- ブロック [`00bafe84`](#insn-00bafe84) 範囲 `[['00bafe84', '00bafe87']]`
  - `FALL_THROUGH` [`00bafe84`](#insn-00bafe84) → [`00bafe88`](#insn-00bafe88)
- ブロック [`00bafe88`](#insn-00bafe88) 範囲 `[['00bafe88', '00bafe9f']]`
  - `CONDITIONAL_JUMP` [`00bafe9c`](#insn-00bafe9c) → [`00bafe08`](#insn-00bafe08)
  - `FALL_THROUGH` [`00bafe9c`](#insn-00bafe9c) → [`00bafea0`](#insn-00bafea0)
- ブロック [`00bafea0`](#insn-00bafea0) 範囲 `[['00bafea0', '00bafea3']]`
  - `CONDITIONAL_JUMP` [`00bafea0`](#insn-00bafea0) → [`00bafe10`](#insn-00bafe10)
  - `FALL_THROUGH` [`00bafea0`](#insn-00bafea0) → [`00bafea4`](#insn-00bafea4)
- ブロック [`00bafea4`](#insn-00bafea4) 範囲 `[['00bafea4', '00bafeab']]`
  - `UNCONDITIONAL_JUMP` [`00bafea8`](#insn-00bafea8) → [`00bafebc`](#insn-00bafebc)
- ブロック [`00bafeac`](#insn-00bafeac) 範囲 `[['00bafeac', '00bafeb3']]`
  - `UNCONDITIONAL_JUMP` [`00bafeb0`](#insn-00bafeb0) → [`00bafebc`](#insn-00bafebc)
- ブロック [`00bafeb4`](#insn-00bafeb4) 範囲 `[['00bafeb4', '00bafebb']]`
  - `FALL_THROUGH` [`00bafeb8`](#insn-00bafeb8) → [`00bafebc`](#insn-00bafebc)
- ブロック [`00bafebc`](#insn-00bafebc) 範囲 `[['00bafebc', '00bafec7']]`
  - `FALL_THROUGH` [`00bafec4`](#insn-00bafec4) → [`00bafec8`](#insn-00bafec8)
- ブロック [`00bafec8`](#insn-00bafec8) 範囲 `[['00bafec8', '00bafedb']]`

## 命令位置別の参照

- [`00bafdbc`](#insn-00bafdbc) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafdc0`](#insn-00bafdc0) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafdc4`](#insn-00bafdc4) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafdc8`](#insn-00bafdc8) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafdcc`](#insn-00bafdcc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafdd0`](#insn-00bafdd0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafde4`](#insn-00bafde4) → [`00bafeac`](#insn-00bafeac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafe04`](#insn-00bafe04) → [`00bafe20`](#insn-00bafe20) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafe0c`](#insn-00bafe0c) → [`00bafea4`](#insn-00bafea4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafe18`](#insn-00bafe18) → [`00bafea4`](#insn-00bafea4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafe40`](#insn-00bafe40) → [`00bafe68`](#insn-00bafe68) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafe58`](#insn-00bafe58) → [`00c58120`](../00c58/00c58120.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58120` · 推定シンボル `None` · 推定型 `None`
- [`00bafe5c`](#insn-00bafe5c) → [`00bafe68`](#insn-00bafe68) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafe60`](#insn-00bafe60) → [`00bafe70`](#insn-00bafe70) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafe64`](#insn-00bafe64) → [`00bafe88`](#insn-00bafe88) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafe6c`](#insn-00bafe6c) → [`00bafe80`](#insn-00bafe80) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafe74`](#insn-00bafe74) → [`00bafeb4`](#insn-00bafeb4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafe7c`](#insn-00bafe7c) → [`00bafe1c`](#insn-00bafe1c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafe80`](#insn-00bafe80) → [`00bafe08`](#insn-00bafe08) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafe98`](#insn-00bafe98) → [`00c58120`](../00c58/00c58120.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58120` · 推定シンボル `None` · 推定型 `None`
- [`00bafe9c`](#insn-00bafe9c) → [`00bafe08`](#insn-00bafe08) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafea0`](#insn-00bafea0) → [`00bafe10`](#insn-00bafe10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafea8`](#insn-00bafea8) → [`00bafebc`](#insn-00bafebc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafeb0`](#insn-00bafeb0) → [`00bafebc`](#insn-00bafebc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafec0`](#insn-00bafec0) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafec4`](#insn-00bafec4) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafec8`](#insn-00bafec8) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafecc`](#insn-00bafecc) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafed0`](#insn-00bafed0) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bafdbc`](#insn-00bafdbc)

~~~json
{
  "source": "00bafdbc",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafdc0`](#insn-00bafdc0)

~~~json
{
  "source": "00bafdc0",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafdc4`](#insn-00bafdc4)

~~~json
{
  "source": "00bafdc4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafdc8`](#insn-00bafdc8)

~~~json
{
  "source": "00bafdc8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafdcc`](#insn-00bafdcc)

~~~json
{
  "source": "00bafdcc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafdd0`](#insn-00bafdd0)

~~~json
{
  "source": "00bafdd0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafde4`](#insn-00bafde4)

~~~json
{
  "source": "00bafde4",
  "target": "00bafeac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafe04`](#insn-00bafe04)

~~~json
{
  "source": "00bafe04",
  "target": "00bafe20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafe0c`](#insn-00bafe0c)

~~~json
{
  "source": "00bafe0c",
  "target": "00bafea4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafe18`](#insn-00bafe18)

~~~json
{
  "source": "00bafe18",
  "target": "00bafea4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafe40`](#insn-00bafe40)

~~~json
{
  "source": "00bafe40",
  "target": "00bafe68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafe58`](#insn-00bafe58)

~~~json
{
  "source": "00bafe58",
  "target": "00c58120",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bafe5c`](#insn-00bafe5c)

~~~json
{
  "source": "00bafe5c",
  "target": "00bafe68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafe60`](#insn-00bafe60)

~~~json
{
  "source": "00bafe60",
  "target": "00bafe70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafe64`](#insn-00bafe64)

~~~json
{
  "source": "00bafe64",
  "target": "00bafe88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafe6c`](#insn-00bafe6c)

~~~json
{
  "source": "00bafe6c",
  "target": "00bafe80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafe74`](#insn-00bafe74)

~~~json
{
  "source": "00bafe74",
  "target": "00bafeb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafe7c`](#insn-00bafe7c)

~~~json
{
  "source": "00bafe7c",
  "target": "00bafe1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafe80`](#insn-00bafe80)

~~~json
{
  "source": "00bafe80",
  "target": "00bafe08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafe98`](#insn-00bafe98)

~~~json
{
  "source": "00bafe98",
  "target": "00c58120",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bafe9c`](#insn-00bafe9c)

~~~json
{
  "source": "00bafe9c",
  "target": "00bafe08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafea0`](#insn-00bafea0)

~~~json
{
  "source": "00bafea0",
  "target": "00bafe10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafea8`](#insn-00bafea8)

~~~json
{
  "source": "00bafea8",
  "target": "00bafebc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafeb0`](#insn-00bafeb0)

~~~json
{
  "source": "00bafeb0",
  "target": "00bafebc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafec0`](#insn-00bafec0)

~~~json
{
  "source": "00bafec0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafec4`](#insn-00bafec4)

~~~json
{
  "source": "00bafec4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafec8`](#insn-00bafec8)

~~~json
{
  "source": "00bafec8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafecc`](#insn-00bafecc)

~~~json
{
  "source": "00bafecc",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafed0`](#insn-00bafed0)

~~~json
{
  "source": "00bafed0",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
