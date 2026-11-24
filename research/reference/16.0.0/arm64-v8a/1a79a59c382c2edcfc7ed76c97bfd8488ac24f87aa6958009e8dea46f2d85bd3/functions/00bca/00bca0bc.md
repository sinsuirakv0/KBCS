# 00bca0bc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b5abbc`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5a/00b5abbc.md) · 移動量 `+0x6f500`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0066.md#compare-7ff749a9d06bf004a637d1896cf0ef3a)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bca4e4`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bca/00bca4e4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0081.md#compare-2a3c368255c41c1e41cde17686a24a49)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bca0bc",
  "name": "_ZN8firebase4auth4Auth7GetAuthEPNS_3AppEPNS_10InitResultE",
  "size": 484,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "6dad339c43cab4b1b8b36f59e52d7668aace67c7c4ebf6a45eec1b52396ca425",
  "source_text_sha256": "6dad339c43cab4b1b8b36f59e52d7668aace67c7c4ebf6a45eec1b52396ca425",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bca0bc",
        "00bca29f"
      ]
    ],
    "bytes_sha256": "fc2a3b7cc0a327af9a78bd35658e12b1b01f3936ee3ec6f241653d8c00c8437b",
    "instruction_count": 121,
    "instruction_bytes": 484,
    "body_bytes": 484,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c5a5c0](../00c5a/00c5a5c0.md)

## 呼び出し先

- [00c57a90](../00c57/00c57a90.md)
- [00c5a600](../00c5a/00c5a600.md)
- [00c5a610](../00c5a/00c5a610.md)
- [00c5ad30](../00c5a/00c5ad30.md)
- [00c5b1e0](../00c5b/00c5b1e0.md)
- [00c5d590](../00c5d/00c5d590.md)
- [00c5d5d0](../00c5d/00c5d5d0.md)
- [00c5d690](../00c5d/00c5d690.md)

## 関連文字列（未確認候補）

~~~text
"Creating Auth %p for App %p"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 3373 bytes

~~~c

long _ZN8firebase4auth4Auth7GetAuthEPNS_3AppEPNS_10InitResultE(ulong param_1,undefined4 *param_2)

{
  undefined *puVar1;
  long lVar2;
  undefined *puVar3;
  undefined *puVar4;
  undefined8 uVar5;
  long lVar6;
  undefined8 uVar7;
  undefined8 *puVar8;
  undefined8 *puVar9;
  undefined8 *puVar10;
  
  puVar1 = PTR__ZN8firebase4auth13g_auths_mutexE_00c9b5a0;
  uVar5 = *(undefined8 *)PTR__ZN8firebase4auth13g_auths_mutexE_00c9b5a0;
  _ZN8firebase5Mutex7AcquireEv(uVar5);
  uVar7 = *(undefined8 *)puVar1;
  _ZN8firebase5Mutex7AcquireEv(uVar7);
  puVar1 = PTR__ZN8firebase4auth7g_authsE_00c9b5a8;
  puVar4 = *(undefined **)(PTR__ZN8firebase4auth7g_authsE_00c9b5a8 + 8);
  if (puVar4 != (undefined *)0x0) {
    puVar3 = PTR__ZN8firebase4auth7g_authsE_00c9b5a8 + 8;
    do {
      if (*(ulong *)(puVar4 + 0x20) >= param_1) {
        puVar3 = puVar4;
      }
      puVar4 = *(undefined **)(puVar4 + (ulong)(*(ulong *)(puVar4 + 0x20) < param_1) * 8);
    } while (puVar4 != (undefined *)0x0);
    if ((puVar3 != PTR__ZN8firebase4auth7g_authsE_00c9b5a8 + 8) &&
       (*(ulong *)(puVar3 + 0x20) <= param_1)) {
      lVar6 = *(long *)(puVar3 + 0x28);
      goto LAB_00bca144;
    }
  }
  lVar6 = 0;
LAB_00bca144:
  _ZN8firebase5Mutex7ReleaseEv(uVar7);
  if (lVar6 == 0) {
    lVar2 = _ZN8firebase4auth18CreatePlatformAuthEPNS_3AppE(param_1);
    if (lVar2 == 0) {
      lVar6 = 0;
    }
    else {
      lVar6 = _Znwm(8);
      _ZN8firebase4auth4AuthC1EPNS_3AppEPv(lVar6,param_1,lVar2);
      _ZN8firebase8LogDebugEPKcz("Creating Auth %p for App %p",lVar6,param_1);
      puVar10 = (undefined8 *)(puVar1 + 8);
      if ((undefined8 *)*puVar10 == (undefined8 *)0x0) {
        puVar8 = (undefined8 *)*puVar10;
        puVar9 = puVar10;
      }
      else {
        puVar8 = (undefined8 *)*puVar10;
        puVar9 = (undefined8 *)(puVar1 + 8);
LAB_00bca1d8:
        do {
          puVar10 = puVar8;
          if ((ulong)puVar10[4] <= param_1) {
            if ((ulong)puVar10[4] < param_1) {
              puVar9 = puVar10 + 1;
              puVar8 = (undefined8 *)*puVar9;
              if ((undefined8 *)*puVar9 != (undefined8 *)0x0) goto LAB_00bca1d8;
            }
            puVar8 = (undefined8 *)*puVar9;
            goto joined_r0x00bca240;
          }
          puVar8 = (undefined8 *)*puVar10;
          puVar9 = puVar10;
        } while ((undefined8 *)*puVar10 != (undefined8 *)0x0);
        puVar8 = (undefined8 *)*puVar10;
      }
joined_r0x00bca240:
      if (puVar8 == (undefined8 *)0x0) {
        puVar8 = (undefined8 *)_Znwm(0x30);
        puVar8[4] = param_1;
        puVar8[5] = 0;
        *puVar8 = 0;
        puVar8[1] = 0;
        puVar8[2] = puVar10;
        *puVar9 = puVar8;
        puVar10 = puVar8;
        if (**(long **)puVar1 != 0) {
          *(long *)puVar1 = **(long **)puVar1;
          puVar10 = (undefined8 *)*puVar9;
        }
        _ZNSt6__ndk127__tree_balance_after_insertIPNS_16__tree_node_baseIPvEEEEvT_S5_
                  (*(undefined8 *)(puVar1 + 8),puVar10);
        *(long *)(puVar1 + 0x10) = *(long *)(puVar1 + 0x10) + 1;
      }
      puVar8[5] = lVar6;
      if (param_2 != (undefined4 *)0x0) {
        *param_2 = 0;
      }
    }
  }
  else {
    if (param_2 != (undefined4 *)0x0) {
      *param_2 = 0;
    }
    _ZN8firebase4auth12LogHeartbeatEPNS0_4AuthE(lVar6);
  }
  _ZN8firebase5Mutex7ReleaseEv(uVar5);
  return lVar6;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bca0bc"></a> `00bca0bc` | `fa 67 bb a9` | stp x26,x25,[sp, #-0x50]! | `FALL_THROUGH`
<a id="insn-00bca0c0"></a> `00bca0c0` | `f8 5f 01 a9` | stp x24,x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bca0c4"></a> `00bca0c4` | `f6 57 02 a9` | stp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bca0c8"></a> `00bca0c8` | `f4 4f 03 a9` | stp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bca0cc"></a> `00bca0cc` | `fd 7b 04 a9` | stp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bca0d0"></a> `00bca0d0` | `fd 03 01 91` | add x29,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00bca0d4"></a> `00bca0d4` | `95 06 00 b0` | adrp x21,0xc9b000 | `FALL_THROUGH`
<a id="insn-00bca0d8"></a> `00bca0d8` | `b5 d2 42 f9` | ldr x21,[x21, #0x5a0] | `FALL_THROUGH`
<a id="insn-00bca0dc"></a> `00bca0dc` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00bca0e0"></a> `00bca0e0` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-00bca0e4"></a> `00bca0e4` | `b3 02 40 f9` | ldr x19,[x21] | `FALL_THROUGH`
<a id="insn-00bca0e8"></a> `00bca0e8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bca0ec"></a> `00bca0ec` | `45 41 02 94` | bl 0x00c5a600 | `UNCONDITIONAL_CALL`
<a id="insn-00bca0f0"></a> `00bca0f0` | `b7 02 40 f9` | ldr x23,[x21] | `FALL_THROUGH`
<a id="insn-00bca0f4"></a> `00bca0f4` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00bca0f8"></a> `00bca0f8` | `42 41 02 94` | bl 0x00c5a600 | `UNCONDITIONAL_CALL`
<a id="insn-00bca0fc"></a> `00bca0fc` | `98 06 00 b0` | adrp x24,0xc9b000 | `FALL_THROUGH`
<a id="insn-00bca100"></a> `00bca100` | `18 d7 42 f9` | ldr x24,[x24, #0x5a8] | `FALL_THROUGH`
<a id="insn-00bca104"></a> `00bca104` | `09 07 40 f9` | ldr x9,[x24, #0x8] | `FALL_THROUGH`
<a id="insn-00bca108"></a> `00bca108` | `c9 01 00 b4` | cbz x9,0x00bca140 | `CONDITIONAL_JUMP`
<a id="insn-00bca10c"></a> `00bca10c` | `08 23 00 91` | add x8,x24,#0x8 | `FALL_THROUGH`
<a id="insn-00bca110"></a> `00bca110` | `2a 11 40 f9` | ldr x10,[x9, #0x20] | `FALL_THROUGH`
<a id="insn-00bca114"></a> `00bca114` | `5f 01 16 eb` | cmp x10,x22 | `FALL_THROUGH`
<a id="insn-00bca118"></a> `00bca118` | `ea 27 9f 1a` | cset w10,cc | `FALL_THROUGH`
<a id="insn-00bca11c"></a> `00bca11c` | `08 31 89 9a` | csel x8,x8,x9,cc | `FALL_THROUGH`
<a id="insn-00bca120"></a> `00bca120` | `29 59 6a f8` | ldr x9,[x9, w10, UXTW #0x3] | `FALL_THROUGH`
<a id="insn-00bca124"></a> `00bca124` | `69 ff ff b5` | cbnz x9,0x00bca110 | `CONDITIONAL_JUMP`
<a id="insn-00bca128"></a> `00bca128` | `09 23 00 91` | add x9,x24,#0x8 | `FALL_THROUGH`
<a id="insn-00bca12c"></a> `00bca12c` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bca130"></a> `00bca130` | `80 00 00 54` | b.eq 0x00bca140 | `CONDITIONAL_JUMP`
<a id="insn-00bca134"></a> `00bca134` | `09 11 40 f9` | ldr x9,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00bca138"></a> `00bca138` | `3f 01 16 eb` | cmp x9,x22 | `FALL_THROUGH`
<a id="insn-00bca13c"></a> `00bca13c` | `c9 06 00 54` | b.ls 0x00bca214 | `CONDITIONAL_JUMP`
<a id="insn-00bca140"></a> `00bca140` | `f5 03 1f aa` | mov x21,xzr | `FALL_THROUGH`
<a id="insn-00bca144"></a> `00bca144` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00bca148"></a> `00bca148` | `32 41 02 94` | bl 0x00c5a610 | `UNCONDITIONAL_CALL`
<a id="insn-00bca14c"></a> `00bca14c` | `d5 01 00 b4` | cbz x21,0x00bca184 | `CONDITIONAL_JUMP`
<a id="insn-00bca150"></a> `00bca150` | `54 00 00 b4` | cbz x20,0x00bca158 | `CONDITIONAL_JUMP`
<a id="insn-00bca154"></a> `00bca154` | `9f 02 00 b9` | str wzr,[x20] | `FALL_THROUGH`
<a id="insn-00bca158"></a> `00bca158` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bca15c"></a> `00bca15c` | `0d 4d 02 94` | bl 0x00c5d590 | `UNCONDITIONAL_CALL`
<a id="insn-00bca160"></a> `00bca160` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bca164"></a> `00bca164` | `2b 41 02 94` | bl 0x00c5a610 | `UNCONDITIONAL_CALL`
<a id="insn-00bca168"></a> `00bca168` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bca16c"></a> `00bca16c` | `fd 7b 44 a9` | ldp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bca170"></a> `00bca170` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bca174"></a> `00bca174` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bca178"></a> `00bca178` | `f8 5f 41 a9` | ldp x24,x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bca17c"></a> `00bca17c` | `fa 67 c5 a8` | ldp x26,x25,[sp], #0x50 | `FALL_THROUGH`
<a id="insn-00bca180"></a> `00bca180` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bca184"></a> `00bca184` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00bca188"></a> `00bca188` | `12 4d 02 94` | bl 0x00c5d5d0 | `UNCONDITIONAL_CALL`
<a id="insn-00bca18c"></a> `00bca18c` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-00bca190"></a> `00bca190` | `60 04 00 b4` | cbz x0,0x00bca21c | `CONDITIONAL_JUMP`
<a id="insn-00bca194"></a> `00bca194` | `00 01 80 52` | mov w0,#0x8 | `FALL_THROUGH`
<a id="insn-00bca198"></a> `00bca198` | `3e 36 02 94` | bl 0x00c57a90 | `UNCONDITIONAL_CALL`
<a id="insn-00bca19c"></a> `00bca19c` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00bca1a0"></a> `00bca1a0` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00bca1a4"></a> `00bca1a4` | `e2 03 17 aa` | mov x2,x23 | `FALL_THROUGH`
<a id="insn-00bca1a8"></a> `00bca1a8` | `3a 4d 02 94` | bl 0x00c5d690 | `UNCONDITIONAL_CALL`
<a id="insn-00bca1ac"></a> `00bca1ac` | `00 b7 ff f0` | adrp x0,0x2ad000 | `FALL_THROUGH`
<a id="insn-00bca1b0"></a> `00bca1b0` | `00 38 0c 91` | add x0,x0,#0x30e | `FALL_THROUGH`
<a id="insn-00bca1b4"></a> `00bca1b4` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00bca1b8"></a> `00bca1b8` | `e2 03 16 aa` | mov x2,x22 | `FALL_THROUGH`
<a id="insn-00bca1bc"></a> `00bca1bc` | `dd 42 02 94` | bl 0x00c5ad30 | `UNCONDITIONAL_CALL`
<a id="insn-00bca1c0"></a> `00bca1c0` | `fa 03 18 aa` | mov x26,x24 | `FALL_THROUGH`
<a id="insn-00bca1c4"></a> `00bca1c4` | `48 8f 40 f8` | ldr x8,[x26, #0x8]! | `FALL_THROUGH`
<a id="insn-00bca1c8"></a> `00bca1c8` | `e8 02 00 b4` | cbz x8,0x00bca224 | `CONDITIONAL_JUMP`
<a id="insn-00bca1cc"></a> `00bca1cc` | `19 23 00 91` | add x25,x24,#0x8 | `FALL_THROUGH`
<a id="insn-00bca1d0"></a> `00bca1d0` | `02 00 00 14` | b 0x00bca1d8 | `UNCONDITIONAL_JUMP`
<a id="insn-00bca1d4"></a> `00bca1d4` | `e8 03 09 aa` | mov x8,x9 | `FALL_THROUGH`
<a id="insn-00bca1d8"></a> `00bca1d8` | `09 11 40 f9` | ldr x9,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00bca1dc"></a> `00bca1dc` | `3f 01 16 eb` | cmp x9,x22 | `FALL_THROUGH`
<a id="insn-00bca1e0"></a> `00bca1e0` | `a9 00 00 54` | b.ls 0x00bca1f4 | `CONDITIONAL_JUMP`
<a id="insn-00bca1e4"></a> `00bca1e4` | `09 01 40 f9` | ldr x9,[x8] | `FALL_THROUGH`
<a id="insn-00bca1e8"></a> `00bca1e8` | `69 02 00 b4` | cbz x9,0x00bca234 | `CONDITIONAL_JUMP`
<a id="insn-00bca1ec"></a> `00bca1ec` | `f9 03 08 aa` | mov x25,x8 | `FALL_THROUGH`
<a id="insn-00bca1f0"></a> `00bca1f0` | `f9 ff ff 17` | b 0x00bca1d4 | `UNCONDITIONAL_JUMP`
<a id="insn-00bca1f4"></a> `00bca1f4` | `82 00 00 54` | b.cs 0x00bca204 | `CONDITIONAL_JUMP`
<a id="insn-00bca1f8"></a> `00bca1f8` | `f9 03 08 aa` | mov x25,x8 | `FALL_THROUGH`
<a id="insn-00bca1fc"></a> `00bca1fc` | `29 8f 40 f8` | ldr x9,[x25, #0x8]! | `FALL_THROUGH`
<a id="insn-00bca200"></a> `00bca200` | `a9 fe ff b5` | cbnz x9,0x00bca1d4 | `CONDITIONAL_JUMP`
<a id="insn-00bca204"></a> `00bca204` | `fa 03 08 aa` | mov x26,x8 | `FALL_THROUGH`
<a id="insn-00bca208"></a> `00bca208` | `37 03 40 f9` | ldr x23,[x25] | `FALL_THROUGH`
<a id="insn-00bca20c"></a> `00bca20c` | `37 04 00 b5` | cbnz x23,0x00bca290 | `CONDITIONAL_JUMP`
<a id="insn-00bca210"></a> `00bca210` | `0d 00 00 14` | b 0x00bca244 | `UNCONDITIONAL_JUMP`
<a id="insn-00bca214"></a> `00bca214` | `15 15 40 f9` | ldr x21,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00bca218"></a> `00bca218` | `cb ff ff 17` | b 0x00bca144 | `UNCONDITIONAL_JUMP`
<a id="insn-00bca21c"></a> `00bca21c` | `f5 03 1f aa` | mov x21,xzr | `FALL_THROUGH`
<a id="insn-00bca220"></a> `00bca220` | `d0 ff ff 17` | b 0x00bca160 | `UNCONDITIONAL_JUMP`
<a id="insn-00bca224"></a> `00bca224` | `f9 03 1a aa` | mov x25,x26 | `FALL_THROUGH`
<a id="insn-00bca228"></a> `00bca228` | `37 03 40 f9` | ldr x23,[x25] | `FALL_THROUGH`
<a id="insn-00bca22c"></a> `00bca22c` | `37 03 00 b5` | cbnz x23,0x00bca290 | `CONDITIONAL_JUMP`
<a id="insn-00bca230"></a> `00bca230` | `05 00 00 14` | b 0x00bca244 | `UNCONDITIONAL_JUMP`
<a id="insn-00bca234"></a> `00bca234` | `fa 03 08 aa` | mov x26,x8 | `FALL_THROUGH`
<a id="insn-00bca238"></a> `00bca238` | `f9 03 08 aa` | mov x25,x8 | `FALL_THROUGH`
<a id="insn-00bca23c"></a> `00bca23c` | `37 03 40 f9` | ldr x23,[x25] | `FALL_THROUGH`
<a id="insn-00bca240"></a> `00bca240` | `97 02 00 b5` | cbnz x23,0x00bca290 | `CONDITIONAL_JUMP`
<a id="insn-00bca244"></a> `00bca244` | `00 06 80 52` | mov w0,#0x30 | `FALL_THROUGH`
<a id="insn-00bca248"></a> `00bca248` | `12 36 02 94` | bl 0x00c57a90 | `UNCONDITIONAL_CALL`
<a id="insn-00bca24c"></a> `00bca24c` | `16 7c 02 a9` | stp x22,xzr,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00bca250"></a> `00bca250` | `1f 7c 00 a9` | stp xzr,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00bca254"></a> `00bca254` | `1a 08 00 f9` | str x26,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00bca258"></a> `00bca258` | `20 03 00 f9` | str x0,[x25] | `FALL_THROUGH`
<a id="insn-00bca25c"></a> `00bca25c` | `08 03 40 f9` | ldr x8,[x24] | `FALL_THROUGH`
<a id="insn-00bca260"></a> `00bca260` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-00bca264"></a> `00bca264` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00bca268"></a> `00bca268` | `88 00 00 b4` | cbz x8,0x00bca278 | `CONDITIONAL_JUMP`
<a id="insn-00bca26c"></a> `00bca26c` | `08 03 00 f9` | str x8,[x24] | `FALL_THROUGH`
<a id="insn-00bca270"></a> `00bca270` | `21 03 40 f9` | ldr x1,[x25] | `FALL_THROUGH`
<a id="insn-00bca274"></a> `00bca274` | `02 00 00 14` | b 0x00bca27c | `UNCONDITIONAL_JUMP`
<a id="insn-00bca278"></a> `00bca278` | `e1 03 17 aa` | mov x1,x23 | `FALL_THROUGH`
<a id="insn-00bca27c"></a> `00bca27c` | `00 07 40 f9` | ldr x0,[x24, #0x8] | `FALL_THROUGH`
<a id="insn-00bca280"></a> `00bca280` | `d8 43 02 94` | bl 0x00c5b1e0 | `UNCONDITIONAL_CALL`
<a id="insn-00bca284"></a> `00bca284` | `08 0b 40 f9` | ldr x8,[x24, #0x10] | `FALL_THROUGH`
<a id="insn-00bca288"></a> `00bca288` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bca28c"></a> `00bca28c` | `08 0b 00 f9` | str x8,[x24, #0x10] | `FALL_THROUGH`
<a id="insn-00bca290"></a> `00bca290` | `f5 16 00 f9` | str x21,[x23, #0x28] | `FALL_THROUGH`
<a id="insn-00bca294"></a> `00bca294` | `74 f6 ff b4` | cbz x20,0x00bca160 | `CONDITIONAL_JUMP`
<a id="insn-00bca298"></a> `00bca298` | `9f 02 00 b9` | str wzr,[x20] | `FALL_THROUGH`
<a id="insn-00bca29c"></a> `00bca29c` | `b1 ff ff 17` | b 0x00bca160 | `UNCONDITIONAL_JUMP`

## 基本ブロックと分岐先

- ブロック [`00bca0bc`](#insn-00bca0bc) 範囲 `[['00bca0bc', '00bca10b']]`
  - `CONDITIONAL_JUMP` [`00bca108`](#insn-00bca108) → [`00bca140`](#insn-00bca140)
  - `FALL_THROUGH` [`00bca108`](#insn-00bca108) → [`00bca10c`](#insn-00bca10c)
- ブロック [`00bca10c`](#insn-00bca10c) 範囲 `[['00bca10c', '00bca10f']]`
  - `FALL_THROUGH` [`00bca10c`](#insn-00bca10c) → [`00bca110`](#insn-00bca110)
- ブロック [`00bca110`](#insn-00bca110) 範囲 `[['00bca110', '00bca127']]`
  - `CONDITIONAL_JUMP` [`00bca124`](#insn-00bca124) → [`00bca110`](#insn-00bca110)
  - `FALL_THROUGH` [`00bca124`](#insn-00bca124) → [`00bca128`](#insn-00bca128)
- ブロック [`00bca128`](#insn-00bca128) 範囲 `[['00bca128', '00bca133']]`
  - `CONDITIONAL_JUMP` [`00bca130`](#insn-00bca130) → [`00bca140`](#insn-00bca140)
  - `FALL_THROUGH` [`00bca130`](#insn-00bca130) → [`00bca134`](#insn-00bca134)
- ブロック [`00bca134`](#insn-00bca134) 範囲 `[['00bca134', '00bca13f']]`
  - `CONDITIONAL_JUMP` [`00bca13c`](#insn-00bca13c) → [`00bca214`](#insn-00bca214)
  - `FALL_THROUGH` [`00bca13c`](#insn-00bca13c) → [`00bca140`](#insn-00bca140)
- ブロック [`00bca140`](#insn-00bca140) 範囲 `[['00bca140', '00bca143']]`
  - `FALL_THROUGH` [`00bca140`](#insn-00bca140) → [`00bca144`](#insn-00bca144)
- ブロック [`00bca144`](#insn-00bca144) 範囲 `[['00bca144', '00bca14f']]`
  - `CONDITIONAL_JUMP` [`00bca14c`](#insn-00bca14c) → [`00bca184`](#insn-00bca184)
  - `FALL_THROUGH` [`00bca14c`](#insn-00bca14c) → [`00bca150`](#insn-00bca150)
- ブロック [`00bca150`](#insn-00bca150) 範囲 `[['00bca150', '00bca153']]`
  - `CONDITIONAL_JUMP` [`00bca150`](#insn-00bca150) → [`00bca158`](#insn-00bca158)
  - `FALL_THROUGH` [`00bca150`](#insn-00bca150) → [`00bca154`](#insn-00bca154)
- ブロック [`00bca154`](#insn-00bca154) 範囲 `[['00bca154', '00bca157']]`
  - `FALL_THROUGH` [`00bca154`](#insn-00bca154) → [`00bca158`](#insn-00bca158)
- ブロック [`00bca158`](#insn-00bca158) 範囲 `[['00bca158', '00bca15f']]`
  - `FALL_THROUGH` [`00bca15c`](#insn-00bca15c) → [`00bca160`](#insn-00bca160)
- ブロック [`00bca160`](#insn-00bca160) 範囲 `[['00bca160', '00bca183']]`
- ブロック [`00bca184`](#insn-00bca184) 範囲 `[['00bca184', '00bca193']]`
  - `CONDITIONAL_JUMP` [`00bca190`](#insn-00bca190) → [`00bca21c`](#insn-00bca21c)
  - `FALL_THROUGH` [`00bca190`](#insn-00bca190) → [`00bca194`](#insn-00bca194)
- ブロック [`00bca194`](#insn-00bca194) 範囲 `[['00bca194', '00bca1cb']]`
  - `CONDITIONAL_JUMP` [`00bca1c8`](#insn-00bca1c8) → [`00bca224`](#insn-00bca224)
  - `FALL_THROUGH` [`00bca1c8`](#insn-00bca1c8) → [`00bca1cc`](#insn-00bca1cc)
- ブロック [`00bca1cc`](#insn-00bca1cc) 範囲 `[['00bca1cc', '00bca1d3']]`
  - `UNCONDITIONAL_JUMP` [`00bca1d0`](#insn-00bca1d0) → [`00bca1d8`](#insn-00bca1d8)
- ブロック [`00bca1d4`](#insn-00bca1d4) 範囲 `[['00bca1d4', '00bca1d7']]`
  - `FALL_THROUGH` [`00bca1d4`](#insn-00bca1d4) → [`00bca1d8`](#insn-00bca1d8)
- ブロック [`00bca1d8`](#insn-00bca1d8) 範囲 `[['00bca1d8', '00bca1e3']]`
  - `CONDITIONAL_JUMP` [`00bca1e0`](#insn-00bca1e0) → [`00bca1f4`](#insn-00bca1f4)
  - `FALL_THROUGH` [`00bca1e0`](#insn-00bca1e0) → [`00bca1e4`](#insn-00bca1e4)
- ブロック [`00bca1e4`](#insn-00bca1e4) 範囲 `[['00bca1e4', '00bca1eb']]`
  - `CONDITIONAL_JUMP` [`00bca1e8`](#insn-00bca1e8) → [`00bca234`](#insn-00bca234)
  - `FALL_THROUGH` [`00bca1e8`](#insn-00bca1e8) → [`00bca1ec`](#insn-00bca1ec)
- ブロック [`00bca1ec`](#insn-00bca1ec) 範囲 `[['00bca1ec', '00bca1f3']]`
  - `UNCONDITIONAL_JUMP` [`00bca1f0`](#insn-00bca1f0) → [`00bca1d4`](#insn-00bca1d4)
- ブロック [`00bca1f4`](#insn-00bca1f4) 範囲 `[['00bca1f4', '00bca1f7']]`
  - `CONDITIONAL_JUMP` [`00bca1f4`](#insn-00bca1f4) → [`00bca204`](#insn-00bca204)
  - `FALL_THROUGH` [`00bca1f4`](#insn-00bca1f4) → [`00bca1f8`](#insn-00bca1f8)
- ブロック [`00bca1f8`](#insn-00bca1f8) 範囲 `[['00bca1f8', '00bca203']]`
  - `CONDITIONAL_JUMP` [`00bca200`](#insn-00bca200) → [`00bca1d4`](#insn-00bca1d4)
  - `FALL_THROUGH` [`00bca200`](#insn-00bca200) → [`00bca204`](#insn-00bca204)
- ブロック [`00bca204`](#insn-00bca204) 範囲 `[['00bca204', '00bca20f']]`
  - `CONDITIONAL_JUMP` [`00bca20c`](#insn-00bca20c) → [`00bca290`](#insn-00bca290)
  - `FALL_THROUGH` [`00bca20c`](#insn-00bca20c) → [`00bca210`](#insn-00bca210)
- ブロック [`00bca210`](#insn-00bca210) 範囲 `[['00bca210', '00bca213']]`
  - `UNCONDITIONAL_JUMP` [`00bca210`](#insn-00bca210) → [`00bca244`](#insn-00bca244)
- ブロック [`00bca214`](#insn-00bca214) 範囲 `[['00bca214', '00bca21b']]`
  - `UNCONDITIONAL_JUMP` [`00bca218`](#insn-00bca218) → [`00bca144`](#insn-00bca144)
- ブロック [`00bca21c`](#insn-00bca21c) 範囲 `[['00bca21c', '00bca223']]`
  - `UNCONDITIONAL_JUMP` [`00bca220`](#insn-00bca220) → [`00bca160`](#insn-00bca160)
- ブロック [`00bca224`](#insn-00bca224) 範囲 `[['00bca224', '00bca22f']]`
  - `CONDITIONAL_JUMP` [`00bca22c`](#insn-00bca22c) → [`00bca290`](#insn-00bca290)
  - `FALL_THROUGH` [`00bca22c`](#insn-00bca22c) → [`00bca230`](#insn-00bca230)
- ブロック [`00bca230`](#insn-00bca230) 範囲 `[['00bca230', '00bca233']]`
  - `UNCONDITIONAL_JUMP` [`00bca230`](#insn-00bca230) → [`00bca244`](#insn-00bca244)
- ブロック [`00bca234`](#insn-00bca234) 範囲 `[['00bca234', '00bca243']]`
  - `CONDITIONAL_JUMP` [`00bca240`](#insn-00bca240) → [`00bca290`](#insn-00bca290)
  - `FALL_THROUGH` [`00bca240`](#insn-00bca240) → [`00bca244`](#insn-00bca244)
- ブロック [`00bca244`](#insn-00bca244) 範囲 `[['00bca244', '00bca26b']]`
  - `CONDITIONAL_JUMP` [`00bca268`](#insn-00bca268) → [`00bca278`](#insn-00bca278)
  - `FALL_THROUGH` [`00bca268`](#insn-00bca268) → [`00bca26c`](#insn-00bca26c)
- ブロック [`00bca26c`](#insn-00bca26c) 範囲 `[['00bca26c', '00bca277']]`
  - `UNCONDITIONAL_JUMP` [`00bca274`](#insn-00bca274) → [`00bca27c`](#insn-00bca27c)
- ブロック [`00bca278`](#insn-00bca278) 範囲 `[['00bca278', '00bca27b']]`
  - `FALL_THROUGH` [`00bca278`](#insn-00bca278) → [`00bca27c`](#insn-00bca27c)
- ブロック [`00bca27c`](#insn-00bca27c) 範囲 `[['00bca27c', '00bca28f']]`
  - `FALL_THROUGH` [`00bca28c`](#insn-00bca28c) → [`00bca290`](#insn-00bca290)
- ブロック [`00bca290`](#insn-00bca290) 範囲 `[['00bca290', '00bca297']]`
  - `CONDITIONAL_JUMP` [`00bca294`](#insn-00bca294) → [`00bca160`](#insn-00bca160)
  - `FALL_THROUGH` [`00bca294`](#insn-00bca294) → [`00bca298`](#insn-00bca298)
- ブロック [`00bca298`](#insn-00bca298) 範囲 `[['00bca298', '00bca29f']]`
  - `UNCONDITIONAL_JUMP` [`00bca29c`](#insn-00bca29c) → [`00bca160`](#insn-00bca160)

## 命令位置別の参照

- [`00bca0bc`](#insn-00bca0bc) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bca0c0`](#insn-00bca0c0) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bca0c4`](#insn-00bca0c4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bca0c8`](#insn-00bca0c8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bca0cc`](#insn-00bca0cc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bca0d8`](#insn-00bca0d8) → `00c9b5a0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bca0e4`](#insn-00bca0e4) → `01126320`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZN8firebase4auth13g_auths_mutexE` · 推定型 `undefined8`
- [`00bca0ec`](#insn-00bca0ec) → [`00c5a600`](../00c5a/00c5a600.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a600` · 推定シンボル `None` · 推定型 `None`
- [`00bca0f0`](#insn-00bca0f0) → `01126320`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZN8firebase4auth13g_auths_mutexE` · 推定型 `undefined8`
- [`00bca0f8`](#insn-00bca0f8) → [`00c5a600`](../00c5a/00c5a600.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a600` · 推定シンボル `None` · 推定型 `None`
- [`00bca100`](#insn-00bca100) → `00c9b5a8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bca104`](#insn-00bca104) → `01126310`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bca108`](#insn-00bca108) → [`00bca140`](#insn-00bca140) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bca124`](#insn-00bca124) → [`00bca110`](#insn-00bca110) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bca130`](#insn-00bca130) → [`00bca140`](#insn-00bca140) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bca13c`](#insn-00bca13c) → [`00bca214`](#insn-00bca214) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bca148`](#insn-00bca148) → [`00c5a610`](../00c5a/00c5a610.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a610` · 推定シンボル `None` · 推定型 `None`
- [`00bca14c`](#insn-00bca14c) → [`00bca184`](#insn-00bca184) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bca150`](#insn-00bca150) → [`00bca158`](#insn-00bca158) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bca15c`](#insn-00bca15c) → [`00c5d590`](../00c5d/00c5d590.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5d590` · 推定シンボル `None` · 推定型 `None`
- [`00bca164`](#insn-00bca164) → [`00c5a610`](../00c5a/00c5a610.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a610` · 推定シンボル `None` · 推定型 `None`
- [`00bca16c`](#insn-00bca16c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bca170`](#insn-00bca170) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bca174`](#insn-00bca174) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bca178`](#insn-00bca178) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bca188`](#insn-00bca188) → [`00c5d5d0`](../00c5d/00c5d5d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5d5d0` · 推定シンボル `None` · 推定型 `None`
- [`00bca190`](#insn-00bca190) → [`00bca21c`](#insn-00bca21c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bca198`](#insn-00bca198) → [`00c57a90`](../00c57/00c57a90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a90` · 推定シンボル `None` · 推定型 `None`
- [`00bca1a8`](#insn-00bca1a8) → [`00c5d690`](../00c5d/00c5d690.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5d690` · 推定シンボル `None` · 推定型 `None`
- [`00bca1b0`](#insn-00bca1b0) → `002ad30e`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bca1bc`](#insn-00bca1bc) → [`00c5ad30`](../00c5a/00c5ad30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ad30` · 推定シンボル `None` · 推定型 `None`
- [`00bca1c4`](#insn-00bca1c4) → `01126310`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bca1c8`](#insn-00bca1c8) → [`00bca224`](#insn-00bca224) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bca1d0`](#insn-00bca1d0) → [`00bca1d8`](#insn-00bca1d8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bca1e0`](#insn-00bca1e0) → [`00bca1f4`](#insn-00bca1f4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bca1e8`](#insn-00bca1e8) → [`00bca234`](#insn-00bca234) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bca1f0`](#insn-00bca1f0) → [`00bca1d4`](#insn-00bca1d4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bca1f4`](#insn-00bca1f4) → [`00bca204`](#insn-00bca204) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bca200`](#insn-00bca200) → [`00bca1d4`](#insn-00bca1d4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bca20c`](#insn-00bca20c) → [`00bca290`](#insn-00bca290) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bca210`](#insn-00bca210) → [`00bca244`](#insn-00bca244) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bca218`](#insn-00bca218) → [`00bca144`](#insn-00bca144) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bca220`](#insn-00bca220) → [`00bca160`](#insn-00bca160) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bca228`](#insn-00bca228) → `01126310`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bca22c`](#insn-00bca22c) → [`00bca290`](#insn-00bca290) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bca230`](#insn-00bca230) → [`00bca244`](#insn-00bca244) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bca240`](#insn-00bca240) → [`00bca290`](#insn-00bca290) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bca248`](#insn-00bca248) → [`00c57a90`](../00c57/00c57a90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a90` · 推定シンボル `None` · 推定型 `None`
- [`00bca25c`](#insn-00bca25c) → `01126308`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZN8firebase4auth7g_authsE` · 推定型 `undefined8`
- [`00bca268`](#insn-00bca268) → [`00bca278`](#insn-00bca278) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bca26c`](#insn-00bca26c) → `01126308`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZN8firebase4auth7g_authsE` · 推定型 `undefined8`
- [`00bca274`](#insn-00bca274) → [`00bca27c`](#insn-00bca27c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bca27c`](#insn-00bca27c) → `01126310`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bca280`](#insn-00bca280) → [`00c5b1e0`](../00c5b/00c5b1e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b1e0` · 推定シンボル `None` · 推定型 `None`
- [`00bca284`](#insn-00bca284) → `01126318`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bca28c`](#insn-00bca28c) → `01126318`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bca294`](#insn-00bca294) → [`00bca160`](#insn-00bca160) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bca29c`](#insn-00bca29c) → [`00bca160`](#insn-00bca160) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bca0bc`](#insn-00bca0bc)

~~~json
{
  "source": "00bca0bc",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bca0c0`](#insn-00bca0c0)

~~~json
{
  "source": "00bca0c0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bca0c4`](#insn-00bca0c4)

~~~json
{
  "source": "00bca0c4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bca0c8`](#insn-00bca0c8)

~~~json
{
  "source": "00bca0c8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bca0cc`](#insn-00bca0cc)

~~~json
{
  "source": "00bca0cc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bca0d8`](#insn-00bca0d8)

~~~json
{
  "source": "00bca0d8",
  "target": "00c9b5a0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9b5a0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bca0e4`](#insn-00bca0e4)

~~~json
{
  "source": "00bca0e4",
  "target": "01126320",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126320",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bca0ec`](#insn-00bca0ec)

~~~json
{
  "source": "00bca0ec",
  "target": "00c5a600",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bca0f0`](#insn-00bca0f0)

~~~json
{
  "source": "00bca0f0",
  "target": "01126320",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126320",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bca0f8`](#insn-00bca0f8)

~~~json
{
  "source": "00bca0f8",
  "target": "00c5a600",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bca100`](#insn-00bca100)

~~~json
{
  "source": "00bca100",
  "target": "00c9b5a8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9b5a8",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bca104`](#insn-00bca104)

~~~json
{
  "source": "00bca104",
  "target": "01126310",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126310",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bca108`](#insn-00bca108)

~~~json
{
  "source": "00bca108",
  "target": "00bca140",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bca124`](#insn-00bca124)

~~~json
{
  "source": "00bca124",
  "target": "00bca110",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bca130`](#insn-00bca130)

~~~json
{
  "source": "00bca130",
  "target": "00bca140",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bca13c`](#insn-00bca13c)

~~~json
{
  "source": "00bca13c",
  "target": "00bca214",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bca148`](#insn-00bca148)

~~~json
{
  "source": "00bca148",
  "target": "00c5a610",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bca14c`](#insn-00bca14c)

~~~json
{
  "source": "00bca14c",
  "target": "00bca184",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bca150`](#insn-00bca150)

~~~json
{
  "source": "00bca150",
  "target": "00bca158",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bca15c`](#insn-00bca15c)

~~~json
{
  "source": "00bca15c",
  "target": "00c5d590",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bca164`](#insn-00bca164)

~~~json
{
  "source": "00bca164",
  "target": "00c5a610",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bca16c`](#insn-00bca16c)

~~~json
{
  "source": "00bca16c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bca170`](#insn-00bca170)

~~~json
{
  "source": "00bca170",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bca174`](#insn-00bca174)

~~~json
{
  "source": "00bca174",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bca178`](#insn-00bca178)

~~~json
{
  "source": "00bca178",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bca188`](#insn-00bca188)

~~~json
{
  "source": "00bca188",
  "target": "00c5d5d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bca190`](#insn-00bca190)

~~~json
{
  "source": "00bca190",
  "target": "00bca21c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bca198`](#insn-00bca198)

~~~json
{
  "source": "00bca198",
  "target": "00c57a90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bca1a8`](#insn-00bca1a8)

~~~json
{
  "source": "00bca1a8",
  "target": "00c5d690",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bca1b0`](#insn-00bca1b0)

~~~json
{
  "source": "00bca1b0",
  "target": "002ad30e",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002ad30e",
  "offset": 0,
  "size": 28,
  "datatype": "string",
  "bytes": "4372656174696e67204175746820257020666f722041707020257000",
  "capture_start": "002ad30e",
  "capture_bytes": 28,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bca1bc`](#insn-00bca1bc)

~~~json
{
  "source": "00bca1bc",
  "target": "00c5ad30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bca1c4`](#insn-00bca1c4)

~~~json
{
  "source": "00bca1c4",
  "target": "01126310",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126310",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bca1c8`](#insn-00bca1c8)

~~~json
{
  "source": "00bca1c8",
  "target": "00bca224",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bca1d0`](#insn-00bca1d0)

~~~json
{
  "source": "00bca1d0",
  "target": "00bca1d8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bca1e0`](#insn-00bca1e0)

~~~json
{
  "source": "00bca1e0",
  "target": "00bca1f4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bca1e8`](#insn-00bca1e8)

~~~json
{
  "source": "00bca1e8",
  "target": "00bca234",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bca1f0`](#insn-00bca1f0)

~~~json
{
  "source": "00bca1f0",
  "target": "00bca1d4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bca1f4`](#insn-00bca1f4)

~~~json
{
  "source": "00bca1f4",
  "target": "00bca204",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bca200`](#insn-00bca200)

~~~json
{
  "source": "00bca200",
  "target": "00bca1d4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bca20c`](#insn-00bca20c)

~~~json
{
  "source": "00bca20c",
  "target": "00bca290",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bca210`](#insn-00bca210)

~~~json
{
  "source": "00bca210",
  "target": "00bca244",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bca218`](#insn-00bca218)

~~~json
{
  "source": "00bca218",
  "target": "00bca144",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bca220`](#insn-00bca220)

~~~json
{
  "source": "00bca220",
  "target": "00bca160",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bca228`](#insn-00bca228)

~~~json
{
  "source": "00bca228",
  "target": "01126310",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126310",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bca22c`](#insn-00bca22c)

~~~json
{
  "source": "00bca22c",
  "target": "00bca290",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bca230`](#insn-00bca230)

~~~json
{
  "source": "00bca230",
  "target": "00bca244",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bca240`](#insn-00bca240)

~~~json
{
  "source": "00bca240",
  "target": "00bca290",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bca248`](#insn-00bca248)

~~~json
{
  "source": "00bca248",
  "target": "00c57a90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bca25c`](#insn-00bca25c)

~~~json
{
  "source": "00bca25c",
  "target": "01126308",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126308",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bca268`](#insn-00bca268)

~~~json
{
  "source": "00bca268",
  "target": "00bca278",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bca26c`](#insn-00bca26c)

~~~json
{
  "source": "00bca26c",
  "target": "01126308",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126308",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bca274`](#insn-00bca274)

~~~json
{
  "source": "00bca274",
  "target": "00bca27c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bca27c`](#insn-00bca27c)

~~~json
{
  "source": "00bca27c",
  "target": "01126310",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126310",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bca280`](#insn-00bca280)

~~~json
{
  "source": "00bca280",
  "target": "00c5b1e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bca284`](#insn-00bca284)

~~~json
{
  "source": "00bca284",
  "target": "01126318",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126318",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bca28c`](#insn-00bca28c)

~~~json
{
  "source": "00bca28c",
  "target": "01126318",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126318",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bca294`](#insn-00bca294)

~~~json
{
  "source": "00bca294",
  "target": "00bca160",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bca29c`](#insn-00bca29c)

~~~json
{
  "source": "00bca29c",
  "target": "00bca160",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
