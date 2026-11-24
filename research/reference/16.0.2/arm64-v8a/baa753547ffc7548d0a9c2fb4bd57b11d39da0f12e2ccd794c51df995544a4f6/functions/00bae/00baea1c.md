# 00baea1c

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bae980`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bae/00bae980.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/inspection-0038.md#compare-5ec2b571d0386ce5a96ede43ed8482a5)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00bafa10`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00baf/00bafa10.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0035.md#compare-e82fa86c12de9a5f6ba8660563c76084)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00baea1c",
  "name": "_ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers7EnumValEEENS_19__map_value_compareIS7_SB_NS_4lessIS7_EELb1EEENS5_ISB_EEE12__find_equalIS7_EERPNS_16__tree_node_baseIPvEERPNS_15__tree_end_nodeISM_EERKT_",
  "size": 288,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "116b286182833466420aae3c858b209a7df07d79b1cfd452349d87706dc74315",
  "source_text_sha256": "116b286182833466420aae3c858b209a7df07d79b1cfd452349d87706dc74315",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00baea1c",
        "00baeb3b"
      ]
    ],
    "bytes_sha256": "e4f19f14b14a349836c0732037ac5dad0fd26bdc958c78be52d4d6977927ae20",
    "instruction_count": 72,
    "instruction_bytes": 288,
    "body_bytes": 288,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c5cfd0](../00c5c/00c5cfd0.md)

## 呼び出し先

- [00c58120](../00c58/00c58120.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2193 bytes

~~~c

long * _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers7EnumValEEENS_19__map_value_compareIS7_SB_NS_4lessIS7_EELb1EEENS5_ISB_EEE12__find_equalIS7_EERPNS_16__tree_node_baseIPvEERPNS_15__tree_end_nodeISM_EERKT_
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
      if (iVar4 < 0) goto LAB_00baead0;
LAB_00baeae8:
      if ((bVar3 & 1) == 0) {
        __s1_00 = (void *)((long)plVar7 + 0x21);
      }
      iVar4 = memcmp(__s1_00,__s1,__n);
      if (iVar4 == 0) goto LAB_00baea68;
      if (-1 < iVar4) goto LAB_00baeb04;
LAB_00baea70:
      plVar5 = plVar7 + 1;
      plVar6 = (long *)*plVar5;
      if ((long *)*plVar5 == (long *)0x0) {
LAB_00baeb04:
        *param_2 = plVar7;
        return plVar5;
      }
    }
    if (uVar1 <= uVar2) {
      if (__n != 0) {
        __s1_00 = (void *)plVar7[6];
        goto LAB_00baeae8;
      }
LAB_00baea68:
      if (uVar2 <= uVar1) goto LAB_00baeb04;
      goto LAB_00baea70;
    }
LAB_00baead0:
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
<a id="insn-00baea1c"></a> `00baea1c` | `fc 6f ba a9` | stp x28,x27,[sp, #-0x60]! | `FALL_THROUGH`
<a id="insn-00baea20"></a> `00baea20` | `fa 67 01 a9` | stp x26,x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00baea24"></a> `00baea24` | `f8 5f 02 a9` | stp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00baea28"></a> `00baea28` | `f6 57 03 a9` | stp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00baea2c"></a> `00baea2c` | `f4 4f 04 a9` | stp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00baea30"></a> `00baea30` | `fd 7b 05 a9` | stp x29,x30,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00baea34"></a> `00baea34` | `fd 43 01 91` | add x29,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00baea38"></a> `00baea38` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00baea3c"></a> `00baea3c` | `97 8e 40 f8` | ldr x23,[x20, #0x8]! | `FALL_THROUGH`
<a id="insn-00baea40"></a> `00baea40` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00baea44"></a> `00baea44` | `57 06 00 b4` | cbz x23,0x00baeb0c | `CONDITIONAL_JUMP`
<a id="insn-00baea48"></a> `00baea48` | `48 00 40 39` | ldrb w8,[x2] | `FALL_THROUGH`
<a id="insn-00baea4c"></a> `00baea4c` | `49 a8 40 a9` | ldp x9,x10,[x2, #0x8] | `FALL_THROUGH`
<a id="insn-00baea50"></a> `00baea50` | `14 20 00 91` | add x20,x0,#0x8 | `FALL_THROUGH`
<a id="insn-00baea54"></a> `00baea54` | `0b fd 41 d3` | lsr x11,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00baea58"></a> `00baea58` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00baea5c"></a> `00baea5c` | `78 01 89 9a` | csel x24,x11,x9,eq | `FALL_THROUGH`
<a id="insn-00baea60"></a> `00baea60` | `55 15 82 9a` | csinc x21,x10,x2,ne | `FALL_THROUGH`
<a id="insn-00baea64"></a> `00baea64` | `07 00 00 14` | b 0x00baea80 | `UNCONDITIONAL_JUMP`
<a id="insn-00baea68"></a> `00baea68` | `3f 03 18 eb` | cmp x25,x24 | `FALL_THROUGH`
<a id="insn-00baea6c"></a> `00baea6c` | `c2 04 00 54` | b.cs 0x00baeb04 | `CONDITIONAL_JUMP`
<a id="insn-00baea70"></a> `00baea70` | `f4 03 17 aa` | mov x20,x23 | `FALL_THROUGH`
<a id="insn-00baea74"></a> `00baea74` | `88 8e 40 f8` | ldr x8,[x20, #0x8]! | `FALL_THROUGH`
<a id="insn-00baea78"></a> `00baea78` | `68 04 00 b4` | cbz x8,0x00baeb04 | `CONDITIONAL_JUMP`
<a id="insn-00baea7c"></a> `00baea7c` | `f7 03 08 aa` | mov x23,x8 | `FALL_THROUGH`
<a id="insn-00baea80"></a> `00baea80` | `fa 03 17 aa` | mov x26,x23 | `FALL_THROUGH`
<a id="insn-00baea84"></a> `00baea84` | `5b 0f 42 38` | ldrb w27,[x26, #0x20]! | `FALL_THROUGH`
<a id="insn-00baea88"></a> `00baea88` | `48 07 40 f9` | ldr x8,[x26, #0x8] | `FALL_THROUGH`
<a id="insn-00baea8c"></a> `00baea8c` | `69 ff 41 d3` | lsr x9,x27,#0x1 | `FALL_THROUGH`
<a id="insn-00baea90"></a> `00baea90` | `7f 03 00 72` | tst w27,#0x1 | `FALL_THROUGH`
<a id="insn-00baea94"></a> `00baea94` | `39 01 88 9a` | csel x25,x9,x8,eq | `FALL_THROUGH`
<a id="insn-00baea98"></a> `00baea98` | `3f 03 18 eb` | cmp x25,x24 | `FALL_THROUGH`
<a id="insn-00baea9c"></a> `00baea9c` | `36 33 98 9a` | csel x22,x25,x24,cc | `FALL_THROUGH`
<a id="insn-00baeaa0"></a> `00baeaa0` | `56 01 00 b4` | cbz x22,0x00baeac8 | `CONDITIONAL_JUMP`
<a id="insn-00baeaa4"></a> `00baeaa4` | `fc 1a 40 f9` | ldr x28,[x23, #0x30] | `FALL_THROUGH`
<a id="insn-00baeaa8"></a> `00baeaa8` | `7f 03 00 72` | tst w27,#0x1 | `FALL_THROUGH`
<a id="insn-00baeaac"></a> `00baeaac` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00baeab0"></a> `00baeab0` | `e2 03 16 aa` | mov x2,x22 | `FALL_THROUGH`
<a id="insn-00baeab4"></a> `00baeab4` | `81 17 9a 9a` | csinc x1,x28,x26,ne | `FALL_THROUGH`
<a id="insn-00baeab8"></a> `00baeab8` | `9a a5 02 94` | bl 0x00c58120 | `UNCONDITIONAL_CALL`
<a id="insn-00baeabc"></a> `00baeabc` | `60 00 00 34` | cbz w0,0x00baeac8 | `CONDITIONAL_JUMP`
<a id="insn-00baeac0"></a> `00baeac0` | `80 00 f8 37` | tbnz w0,#0x1f,0x00baead0 | `CONDITIONAL_JUMP`
<a id="insn-00baeac4"></a> `00baeac4` | `09 00 00 14` | b 0x00baeae8 | `UNCONDITIONAL_JUMP`
<a id="insn-00baeac8"></a> `00baeac8` | `1f 03 19 eb` | cmp x24,x25 | `FALL_THROUGH`
<a id="insn-00baeacc"></a> `00baeacc` | `a2 00 00 54` | b.cs 0x00baeae0 | `CONDITIONAL_JUMP`
<a id="insn-00baead0"></a> `00baead0` | `e8 02 40 f9` | ldr x8,[x23] | `FALL_THROUGH`
<a id="insn-00baead4"></a> `00baead4` | `08 02 00 b4` | cbz x8,0x00baeb14 | `CONDITIONAL_JUMP`
<a id="insn-00baead8"></a> `00baead8` | `f4 03 17 aa` | mov x20,x23 | `FALL_THROUGH`
<a id="insn-00baeadc"></a> `00baeadc` | `e8 ff ff 17` | b 0x00baea7c | `UNCONDITIONAL_JUMP`
<a id="insn-00baeae0"></a> `00baeae0` | `56 fc ff b4` | cbz x22,0x00baea68 | `CONDITIONAL_JUMP`
<a id="insn-00baeae4"></a> `00baeae4` | `fc 1a 40 f9` | ldr x28,[x23, #0x30] | `FALL_THROUGH`
<a id="insn-00baeae8"></a> `00baeae8` | `7f 03 00 72` | tst w27,#0x1 | `FALL_THROUGH`
<a id="insn-00baeaec"></a> `00baeaec` | `80 17 9a 9a` | csinc x0,x28,x26,ne | `FALL_THROUGH`
<a id="insn-00baeaf0"></a> `00baeaf0` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00baeaf4"></a> `00baeaf4` | `e2 03 16 aa` | mov x2,x22 | `FALL_THROUGH`
<a id="insn-00baeaf8"></a> `00baeaf8` | `8a a5 02 94` | bl 0x00c58120 | `UNCONDITIONAL_CALL`
<a id="insn-00baeafc"></a> `00baeafc` | `60 fb ff 34` | cbz w0,0x00baea68 | `CONDITIONAL_JUMP`
<a id="insn-00baeb00"></a> `00baeb00` | `80 fb ff 37` | tbnz w0,#0x1f,0x00baea70 | `CONDITIONAL_JUMP`
<a id="insn-00baeb04"></a> `00baeb04` | `77 02 00 f9` | str x23,[x19] | `FALL_THROUGH`
<a id="insn-00baeb08"></a> `00baeb08` | `05 00 00 14` | b 0x00baeb1c | `UNCONDITIONAL_JUMP`
<a id="insn-00baeb0c"></a> `00baeb0c` | `74 02 00 f9` | str x20,[x19] | `FALL_THROUGH`
<a id="insn-00baeb10"></a> `00baeb10` | `03 00 00 14` | b 0x00baeb1c | `UNCONDITIONAL_JUMP`
<a id="insn-00baeb14"></a> `00baeb14` | `77 02 00 f9` | str x23,[x19] | `FALL_THROUGH`
<a id="insn-00baeb18"></a> `00baeb18` | `f4 03 17 aa` | mov x20,x23 | `FALL_THROUGH`
<a id="insn-00baeb1c"></a> `00baeb1c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00baeb20"></a> `00baeb20` | `fd 7b 45 a9` | ldp x29,x30,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00baeb24"></a> `00baeb24` | `f4 4f 44 a9` | ldp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00baeb28"></a> `00baeb28` | `f6 57 43 a9` | ldp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00baeb2c"></a> `00baeb2c` | `f8 5f 42 a9` | ldp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00baeb30"></a> `00baeb30` | `fa 67 41 a9` | ldp x26,x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00baeb34"></a> `00baeb34` | `fc 6f c6 a8` | ldp x28,x27,[sp], #0x60 | `FALL_THROUGH`
<a id="insn-00baeb38"></a> `00baeb38` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00baea1c`](#insn-00baea1c) 範囲 `[['00baea1c', '00baea47']]`
  - `CONDITIONAL_JUMP` [`00baea44`](#insn-00baea44) → [`00baeb0c`](#insn-00baeb0c)
  - `FALL_THROUGH` [`00baea44`](#insn-00baea44) → [`00baea48`](#insn-00baea48)
- ブロック [`00baea48`](#insn-00baea48) 範囲 `[['00baea48', '00baea67']]`
  - `UNCONDITIONAL_JUMP` [`00baea64`](#insn-00baea64) → [`00baea80`](#insn-00baea80)
- ブロック [`00baea68`](#insn-00baea68) 範囲 `[['00baea68', '00baea6f']]`
  - `CONDITIONAL_JUMP` [`00baea6c`](#insn-00baea6c) → [`00baeb04`](#insn-00baeb04)
  - `FALL_THROUGH` [`00baea6c`](#insn-00baea6c) → [`00baea70`](#insn-00baea70)
- ブロック [`00baea70`](#insn-00baea70) 範囲 `[['00baea70', '00baea7b']]`
  - `CONDITIONAL_JUMP` [`00baea78`](#insn-00baea78) → [`00baeb04`](#insn-00baeb04)
  - `FALL_THROUGH` [`00baea78`](#insn-00baea78) → [`00baea7c`](#insn-00baea7c)
- ブロック [`00baea7c`](#insn-00baea7c) 範囲 `[['00baea7c', '00baea7f']]`
  - `FALL_THROUGH` [`00baea7c`](#insn-00baea7c) → [`00baea80`](#insn-00baea80)
- ブロック [`00baea80`](#insn-00baea80) 範囲 `[['00baea80', '00baeaa3']]`
  - `CONDITIONAL_JUMP` [`00baeaa0`](#insn-00baeaa0) → [`00baeac8`](#insn-00baeac8)
  - `FALL_THROUGH` [`00baeaa0`](#insn-00baeaa0) → [`00baeaa4`](#insn-00baeaa4)
- ブロック [`00baeaa4`](#insn-00baeaa4) 範囲 `[['00baeaa4', '00baeabf']]`
  - `CONDITIONAL_JUMP` [`00baeabc`](#insn-00baeabc) → [`00baeac8`](#insn-00baeac8)
  - `FALL_THROUGH` [`00baeabc`](#insn-00baeabc) → [`00baeac0`](#insn-00baeac0)
- ブロック [`00baeac0`](#insn-00baeac0) 範囲 `[['00baeac0', '00baeac3']]`
  - `CONDITIONAL_JUMP` [`00baeac0`](#insn-00baeac0) → [`00baead0`](#insn-00baead0)
  - `FALL_THROUGH` [`00baeac0`](#insn-00baeac0) → [`00baeac4`](#insn-00baeac4)
- ブロック [`00baeac4`](#insn-00baeac4) 範囲 `[['00baeac4', '00baeac7']]`
  - `UNCONDITIONAL_JUMP` [`00baeac4`](#insn-00baeac4) → [`00baeae8`](#insn-00baeae8)
- ブロック [`00baeac8`](#insn-00baeac8) 範囲 `[['00baeac8', '00baeacf']]`
  - `CONDITIONAL_JUMP` [`00baeacc`](#insn-00baeacc) → [`00baeae0`](#insn-00baeae0)
  - `FALL_THROUGH` [`00baeacc`](#insn-00baeacc) → [`00baead0`](#insn-00baead0)
- ブロック [`00baead0`](#insn-00baead0) 範囲 `[['00baead0', '00baead7']]`
  - `CONDITIONAL_JUMP` [`00baead4`](#insn-00baead4) → [`00baeb14`](#insn-00baeb14)
  - `FALL_THROUGH` [`00baead4`](#insn-00baead4) → [`00baead8`](#insn-00baead8)
- ブロック [`00baead8`](#insn-00baead8) 範囲 `[['00baead8', '00baeadf']]`
  - `UNCONDITIONAL_JUMP` [`00baeadc`](#insn-00baeadc) → [`00baea7c`](#insn-00baea7c)
- ブロック [`00baeae0`](#insn-00baeae0) 範囲 `[['00baeae0', '00baeae3']]`
  - `CONDITIONAL_JUMP` [`00baeae0`](#insn-00baeae0) → [`00baea68`](#insn-00baea68)
  - `FALL_THROUGH` [`00baeae0`](#insn-00baeae0) → [`00baeae4`](#insn-00baeae4)
- ブロック [`00baeae4`](#insn-00baeae4) 範囲 `[['00baeae4', '00baeae7']]`
  - `FALL_THROUGH` [`00baeae4`](#insn-00baeae4) → [`00baeae8`](#insn-00baeae8)
- ブロック [`00baeae8`](#insn-00baeae8) 範囲 `[['00baeae8', '00baeaff']]`
  - `CONDITIONAL_JUMP` [`00baeafc`](#insn-00baeafc) → [`00baea68`](#insn-00baea68)
  - `FALL_THROUGH` [`00baeafc`](#insn-00baeafc) → [`00baeb00`](#insn-00baeb00)
- ブロック [`00baeb00`](#insn-00baeb00) 範囲 `[['00baeb00', '00baeb03']]`
  - `CONDITIONAL_JUMP` [`00baeb00`](#insn-00baeb00) → [`00baea70`](#insn-00baea70)
  - `FALL_THROUGH` [`00baeb00`](#insn-00baeb00) → [`00baeb04`](#insn-00baeb04)
- ブロック [`00baeb04`](#insn-00baeb04) 範囲 `[['00baeb04', '00baeb0b']]`
  - `UNCONDITIONAL_JUMP` [`00baeb08`](#insn-00baeb08) → [`00baeb1c`](#insn-00baeb1c)
- ブロック [`00baeb0c`](#insn-00baeb0c) 範囲 `[['00baeb0c', '00baeb13']]`
  - `UNCONDITIONAL_JUMP` [`00baeb10`](#insn-00baeb10) → [`00baeb1c`](#insn-00baeb1c)
- ブロック [`00baeb14`](#insn-00baeb14) 範囲 `[['00baeb14', '00baeb1b']]`
  - `FALL_THROUGH` [`00baeb18`](#insn-00baeb18) → [`00baeb1c`](#insn-00baeb1c)
- ブロック [`00baeb1c`](#insn-00baeb1c) 範囲 `[['00baeb1c', '00baeb3b']]`

## 命令位置別の参照

- [`00baea1c`](#insn-00baea1c) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baea20`](#insn-00baea20) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baea24`](#insn-00baea24) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baea28`](#insn-00baea28) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baea2c`](#insn-00baea2c) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baea30`](#insn-00baea30) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baea44`](#insn-00baea44) → [`00baeb0c`](#insn-00baeb0c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baea64`](#insn-00baea64) → [`00baea80`](#insn-00baea80) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baea6c`](#insn-00baea6c) → [`00baeb04`](#insn-00baeb04) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baea78`](#insn-00baea78) → [`00baeb04`](#insn-00baeb04) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baeaa0`](#insn-00baeaa0) → [`00baeac8`](#insn-00baeac8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baeab8`](#insn-00baeab8) → [`00c58120`](../00c58/00c58120.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58120` · 推定シンボル `None` · 推定型 `None`
- [`00baeabc`](#insn-00baeabc) → [`00baeac8`](#insn-00baeac8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baeac0`](#insn-00baeac0) → [`00baead0`](#insn-00baead0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baeac4`](#insn-00baeac4) → [`00baeae8`](#insn-00baeae8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baeacc`](#insn-00baeacc) → [`00baeae0`](#insn-00baeae0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baead4`](#insn-00baead4) → [`00baeb14`](#insn-00baeb14) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baeadc`](#insn-00baeadc) → [`00baea7c`](#insn-00baea7c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baeae0`](#insn-00baeae0) → [`00baea68`](#insn-00baea68) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baeaf8`](#insn-00baeaf8) → [`00c58120`](../00c58/00c58120.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58120` · 推定シンボル `None` · 推定型 `None`
- [`00baeafc`](#insn-00baeafc) → [`00baea68`](#insn-00baea68) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baeb00`](#insn-00baeb00) → [`00baea70`](#insn-00baea70) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baeb08`](#insn-00baeb08) → [`00baeb1c`](#insn-00baeb1c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baeb10`](#insn-00baeb10) → [`00baeb1c`](#insn-00baeb1c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baeb20`](#insn-00baeb20) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baeb24`](#insn-00baeb24) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baeb28`](#insn-00baeb28) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baeb2c`](#insn-00baeb2c) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baeb30`](#insn-00baeb30) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00baea1c`](#insn-00baea1c)

~~~json
{
  "source": "00baea1c",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baea20`](#insn-00baea20)

~~~json
{
  "source": "00baea20",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baea24`](#insn-00baea24)

~~~json
{
  "source": "00baea24",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baea28`](#insn-00baea28)

~~~json
{
  "source": "00baea28",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baea2c`](#insn-00baea2c)

~~~json
{
  "source": "00baea2c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baea30`](#insn-00baea30)

~~~json
{
  "source": "00baea30",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baea44`](#insn-00baea44)

~~~json
{
  "source": "00baea44",
  "target": "00baeb0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baea64`](#insn-00baea64)

~~~json
{
  "source": "00baea64",
  "target": "00baea80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baea6c`](#insn-00baea6c)

~~~json
{
  "source": "00baea6c",
  "target": "00baeb04",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baea78`](#insn-00baea78)

~~~json
{
  "source": "00baea78",
  "target": "00baeb04",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baeaa0`](#insn-00baeaa0)

~~~json
{
  "source": "00baeaa0",
  "target": "00baeac8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baeab8`](#insn-00baeab8)

~~~json
{
  "source": "00baeab8",
  "target": "00c58120",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baeabc`](#insn-00baeabc)

~~~json
{
  "source": "00baeabc",
  "target": "00baeac8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baeac0`](#insn-00baeac0)

~~~json
{
  "source": "00baeac0",
  "target": "00baead0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baeac4`](#insn-00baeac4)

~~~json
{
  "source": "00baeac4",
  "target": "00baeae8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baeacc`](#insn-00baeacc)

~~~json
{
  "source": "00baeacc",
  "target": "00baeae0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baead4`](#insn-00baead4)

~~~json
{
  "source": "00baead4",
  "target": "00baeb14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baeadc`](#insn-00baeadc)

~~~json
{
  "source": "00baeadc",
  "target": "00baea7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baeae0`](#insn-00baeae0)

~~~json
{
  "source": "00baeae0",
  "target": "00baea68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baeaf8`](#insn-00baeaf8)

~~~json
{
  "source": "00baeaf8",
  "target": "00c58120",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baeafc`](#insn-00baeafc)

~~~json
{
  "source": "00baeafc",
  "target": "00baea68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baeb00`](#insn-00baeb00)

~~~json
{
  "source": "00baeb00",
  "target": "00baea70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baeb08`](#insn-00baeb08)

~~~json
{
  "source": "00baeb08",
  "target": "00baeb1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baeb10`](#insn-00baeb10)

~~~json
{
  "source": "00baeb10",
  "target": "00baeb1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baeb20`](#insn-00baeb20)

~~~json
{
  "source": "00baeb20",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baeb24`](#insn-00baeb24)

~~~json
{
  "source": "00baeb24",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baeb28`](#insn-00baeb28)

~~~json
{
  "source": "00baeb28",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baeb2c`](#insn-00baeb2c)

~~~json
{
  "source": "00baeb2c",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baeb30`](#insn-00baeb30)

~~~json
{
  "source": "00baeb30",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
