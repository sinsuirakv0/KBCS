# 00bcadb4

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b5b8b4`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5b/00b5b8b4.md) · 移動量 `+0x6f500`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/alignment_unresolved-0017.md#compare-f022c8bc5ee2d8e9b979d86eec48c71c)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bcb1dc`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcb/00bcb1dc.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/alignment_unresolved-0010.md#compare-ef2551f47c204698318a9892909c5340)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bcadb4",
  "name": "_ZN8firebase4auth4Auth23RemoveAuthStateListenerEPNS0_17AuthStateListenerE",
  "size": 272,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "76e004d4d0c8f41b0f194e0e9d8a3dcfdd2c98a18eb07c26d7758ae77c8b88c6",
  "source_text_sha256": "76e004d4d0c8f41b0f194e0e9d8a3dcfdd2c98a18eb07c26d7758ae77c8b88c6",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bcadb4",
        "00bcaec3"
      ]
    ],
    "bytes_sha256": "b19c9852d34414e357f1be9058983aef2a2fa619f660e59b69d71f686b6f5ef5",
    "instruction_count": 68,
    "instruction_bytes": 272,
    "body_bytes": 272,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c5d670](../00c5d/00c5d670.md)

## 呼び出し先

- [00c5a600](../00c5a/00c5a600.md)
- [00c5a610](../00c5a/00c5a610.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1994 bytes

~~~c

void _ZN8firebase4auth4Auth23RemoveAuthStateListenerEPNS0_17AuthStateListenerE
               (long *param_1,long param_2)

{
  long *plVar1;
  long *plVar2;
  long *plVar3;
  long lVar4;
  
  lVar4 = *param_1;
  if (lVar4 != 0) {
    _ZN8firebase5Mutex7AcquireEv(lVar4 + 0x268);
    plVar3 = *(long **)(lVar4 + 0x230);
    plVar2 = *(long **)(lVar4 + 0x238);
    if (plVar2 != plVar3) {
      if (*plVar3 != param_2) {
        do {
          if (plVar2 + -1 == plVar3) goto LAB_00bcae48;
          plVar1 = plVar3 + 1;
          plVar3 = plVar3 + 1;
        } while (*plVar1 != param_2);
      }
      if (plVar3 != plVar2) {
        if (plVar2 + -1 != plVar3) {
          *plVar3 = plVar2[-1];
          plVar2 = *(long **)(lVar4 + 0x238);
        }
        *(long **)(lVar4 + 0x238) = plVar2 + -1;
      }
    }
LAB_00bcae48:
    plVar3 = *(long **)(param_2 + 8);
    plVar2 = *(long **)(param_2 + 0x10);
    if (plVar2 != plVar3) {
      if ((long *)*plVar3 != param_1) {
        do {
                    /* catch(type#1 @ 00000000) { ... } // from try @ 00bcaedc with catch @ 00bcae6c
                       catch(type#1 @ 00000000) { ... } // from try @ 00bcaf0c with catch @ 00bcae6c
                       catch(type#1 @ 00000000) { ... } // from try @ 00bcaf40 with catch @ 00bcae6c
                       catch(type#1 @ 00000000) { ... } // from try @ 00bcaf68 with catch @ 00bcae6c
                       catch(type#1 @ 00000000) { ... } // from try @ 00bcaf94 with catch @ 00bcae6c
                        */
          if (plVar2 + -1 == plVar3) goto LAB_00bcaeac;
          plVar1 = plVar3 + 1;
          plVar3 = plVar3 + 1;
        } while ((long *)*plVar1 != param_1);
      }
      if (plVar3 != plVar2) {
        if (plVar2 + -1 != plVar3) {
          *plVar3 = plVar2[-1];
          plVar2 = *(long **)(param_2 + 0x10);
        }
        *(long **)(param_2 + 0x10) = plVar2 + -1;
      }
    }
LAB_00bcaeac:
    _ZN8firebase5Mutex7ReleaseEv(lVar4 + 0x268);
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bcadb4"></a> `00bcadb4` | `f6 57 bd a9` | stp x22,x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00bcadb8"></a> `00bcadb8` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcadbc"></a> `00bcadbc` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcadc0"></a> `00bcadc0` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bcadc4"></a> `00bcadc4` | `16 00 40 f9` | ldr x22,[x0] | `FALL_THROUGH`
<a id="insn-00bcadc8"></a> `00bcadc8` | `76 07 00 b4` | cbz x22,0x00bcaeb4 | `CONDITIONAL_JUMP`
<a id="insn-00bcadcc"></a> `00bcadcc` | `d4 a2 09 91` | add x20,x22,#0x268 | `FALL_THROUGH`
<a id="insn-00bcadd0"></a> `00bcadd0` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00bcadd4"></a> `00bcadd4` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bcadd8"></a> `00bcadd8` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00bcaddc"></a> `00bcaddc` | `09 3e 02 94` | bl 0x00c5a600 | `UNCONDITIONAL_CALL`
<a id="insn-00bcade0"></a> `00bcade0` | `c9 1a 41 f9` | ldr x9,[x22, #0x230] | `FALL_THROUGH`
<a id="insn-00bcade4"></a> `00bcade4` | `c8 1e 41 f9` | ldr x8,[x22, #0x238] | `FALL_THROUGH`
<a id="insn-00bcade8"></a> `00bcade8` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bcadec"></a> `00bcadec` | `e0 02 00 54` | b.eq 0x00bcae48 | `CONDITIONAL_JUMP`
<a id="insn-00bcadf0"></a> `00bcadf0` | `2a 01 40 f9` | ldr x10,[x9] | `FALL_THROUGH`
<a id="insn-00bcadf4"></a> `00bcadf4` | `5f 01 13 eb` | cmp x10,x19 | `FALL_THROUGH`
<a id="insn-00bcadf8"></a> `00bcadf8` | `40 01 00 54` | b.eq 0x00bcae20 | `CONDITIONAL_JUMP`
<a id="insn-00bcadfc"></a> `00bcadfc` | `0a 21 00 d1` | sub x10,x8,#0x8 | `FALL_THROUGH`
<a id="insn-00bcae00"></a> `00bcae00` | `eb 03 09 aa` | mov x11,x9 | `FALL_THROUGH`
<a id="insn-00bcae04"></a> `00bcae04` | `5f 01 0b eb` | cmp x10,x11 | `FALL_THROUGH`
<a id="insn-00bcae08"></a> `00bcae08` | `00 02 00 54` | b.eq 0x00bcae48 | `CONDITIONAL_JUMP`
<a id="insn-00bcae0c"></a> `00bcae0c` | `6c 05 40 f9` | ldr x12,[x11, #0x8] | `FALL_THROUGH`
<a id="insn-00bcae10"></a> `00bcae10` | `69 21 00 91` | add x9,x11,#0x8 | `FALL_THROUGH`
<a id="insn-00bcae14"></a> `00bcae14` | `eb 03 09 aa` | mov x11,x9 | `FALL_THROUGH`
<a id="insn-00bcae18"></a> `00bcae18` | `9f 01 13 eb` | cmp x12,x19 | `FALL_THROUGH`
<a id="insn-00bcae1c"></a> `00bcae1c` | `41 ff ff 54` | b.ne 0x00bcae04 | `CONDITIONAL_JUMP`
<a id="insn-00bcae20"></a> `00bcae20` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bcae24"></a> `00bcae24` | `20 01 00 54` | b.eq 0x00bcae48 | `CONDITIONAL_JUMP`
<a id="insn-00bcae28"></a> `00bcae28` | `0a 21 00 d1` | sub x10,x8,#0x8 | `FALL_THROUGH`
<a id="insn-00bcae2c"></a> `00bcae2c` | `5f 01 09 eb` | cmp x10,x9 | `FALL_THROUGH`
<a id="insn-00bcae30"></a> `00bcae30` | `80 00 00 54` | b.eq 0x00bcae40 | `CONDITIONAL_JUMP`
<a id="insn-00bcae34"></a> `00bcae34` | `48 01 40 f9` | ldr x8,[x10] | `FALL_THROUGH`
<a id="insn-00bcae38"></a> `00bcae38` | `28 01 00 f9` | str x8,[x9] | `FALL_THROUGH`
<a id="insn-00bcae3c"></a> `00bcae3c` | `c8 1e 41 f9` | ldr x8,[x22, #0x238] | `FALL_THROUGH`
<a id="insn-00bcae40"></a> `00bcae40` | `08 21 00 d1` | sub x8,x8,#0x8 | `FALL_THROUGH`
<a id="insn-00bcae44"></a> `00bcae44` | `c8 1e 01 f9` | str x8,[x22, #0x238] | `FALL_THROUGH`
<a id="insn-00bcae48"></a> `00bcae48` | `69 a2 40 a9` | ldp x9,x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcae4c"></a> `00bcae4c` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bcae50"></a> `00bcae50` | `e0 02 00 54` | b.eq 0x00bcaeac | `CONDITIONAL_JUMP`
<a id="insn-00bcae54"></a> `00bcae54` | `2a 01 40 f9` | ldr x10,[x9] | `FALL_THROUGH`
<a id="insn-00bcae58"></a> `00bcae58` | `5f 01 15 eb` | cmp x10,x21 | `FALL_THROUGH`
<a id="insn-00bcae5c"></a> `00bcae5c` | `40 01 00 54` | b.eq 0x00bcae84 | `CONDITIONAL_JUMP`
<a id="insn-00bcae60"></a> `00bcae60` | `0a 21 00 d1` | sub x10,x8,#0x8 | `FALL_THROUGH`
<a id="insn-00bcae64"></a> `00bcae64` | `eb 03 09 aa` | mov x11,x9 | `FALL_THROUGH`
<a id="insn-00bcae68"></a> `00bcae68` | `5f 01 0b eb` | cmp x10,x11 | `FALL_THROUGH`
<a id="insn-00bcae6c"></a> `00bcae6c` | `00 02 00 54` | b.eq 0x00bcaeac | `CONDITIONAL_JUMP`
<a id="insn-00bcae70"></a> `00bcae70` | `6c 05 40 f9` | ldr x12,[x11, #0x8] | `FALL_THROUGH`
<a id="insn-00bcae74"></a> `00bcae74` | `69 21 00 91` | add x9,x11,#0x8 | `FALL_THROUGH`
<a id="insn-00bcae78"></a> `00bcae78` | `eb 03 09 aa` | mov x11,x9 | `FALL_THROUGH`
<a id="insn-00bcae7c"></a> `00bcae7c` | `9f 01 15 eb` | cmp x12,x21 | `FALL_THROUGH`
<a id="insn-00bcae80"></a> `00bcae80` | `41 ff ff 54` | b.ne 0x00bcae68 | `CONDITIONAL_JUMP`
<a id="insn-00bcae84"></a> `00bcae84` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bcae88"></a> `00bcae88` | `20 01 00 54` | b.eq 0x00bcaeac | `CONDITIONAL_JUMP`
<a id="insn-00bcae8c"></a> `00bcae8c` | `0a 21 00 d1` | sub x10,x8,#0x8 | `FALL_THROUGH`
<a id="insn-00bcae90"></a> `00bcae90` | `5f 01 09 eb` | cmp x10,x9 | `FALL_THROUGH`
<a id="insn-00bcae94"></a> `00bcae94` | `80 00 00 54` | b.eq 0x00bcaea4 | `CONDITIONAL_JUMP`
<a id="insn-00bcae98"></a> `00bcae98` | `48 01 40 f9` | ldr x8,[x10] | `FALL_THROUGH`
<a id="insn-00bcae9c"></a> `00bcae9c` | `28 01 00 f9` | str x8,[x9] | `FALL_THROUGH`
<a id="insn-00bcaea0"></a> `00bcaea0` | `68 0a 40 f9` | ldr x8,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bcaea4"></a> `00bcaea4` | `08 21 00 d1` | sub x8,x8,#0x8 | `FALL_THROUGH`
<a id="insn-00bcaea8"></a> `00bcaea8` | `68 0a 00 f9` | str x8,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bcaeac"></a> `00bcaeac` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bcaeb0"></a> `00bcaeb0` | `d8 3d 02 94` | bl 0x00c5a610 | `UNCONDITIONAL_CALL`
<a id="insn-00bcaeb4"></a> `00bcaeb4` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcaeb8"></a> `00bcaeb8` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcaebc"></a> `00bcaebc` | `f6 57 c3 a8` | ldp x22,x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bcaec0"></a> `00bcaec0` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bcadb4`](#insn-00bcadb4) 範囲 `[['00bcadb4', '00bcadcb']]`
  - `CONDITIONAL_JUMP` [`00bcadc8`](#insn-00bcadc8) → [`00bcaeb4`](#insn-00bcaeb4)
  - `FALL_THROUGH` [`00bcadc8`](#insn-00bcadc8) → [`00bcadcc`](#insn-00bcadcc)
- ブロック [`00bcadcc`](#insn-00bcadcc) 範囲 `[['00bcadcc', '00bcadef']]`
  - `CONDITIONAL_JUMP` [`00bcadec`](#insn-00bcadec) → [`00bcae48`](#insn-00bcae48)
  - `FALL_THROUGH` [`00bcadec`](#insn-00bcadec) → [`00bcadf0`](#insn-00bcadf0)
- ブロック [`00bcadf0`](#insn-00bcadf0) 範囲 `[['00bcadf0', '00bcadfb']]`
  - `CONDITIONAL_JUMP` [`00bcadf8`](#insn-00bcadf8) → [`00bcae20`](#insn-00bcae20)
  - `FALL_THROUGH` [`00bcadf8`](#insn-00bcadf8) → [`00bcadfc`](#insn-00bcadfc)
- ブロック [`00bcadfc`](#insn-00bcadfc) 範囲 `[['00bcadfc', '00bcae03']]`
  - `FALL_THROUGH` [`00bcae00`](#insn-00bcae00) → [`00bcae04`](#insn-00bcae04)
- ブロック [`00bcae04`](#insn-00bcae04) 範囲 `[['00bcae04', '00bcae0b']]`
  - `CONDITIONAL_JUMP` [`00bcae08`](#insn-00bcae08) → [`00bcae48`](#insn-00bcae48)
  - `FALL_THROUGH` [`00bcae08`](#insn-00bcae08) → [`00bcae0c`](#insn-00bcae0c)
- ブロック [`00bcae0c`](#insn-00bcae0c) 範囲 `[['00bcae0c', '00bcae1f']]`
  - `CONDITIONAL_JUMP` [`00bcae1c`](#insn-00bcae1c) → [`00bcae04`](#insn-00bcae04)
  - `FALL_THROUGH` [`00bcae1c`](#insn-00bcae1c) → [`00bcae20`](#insn-00bcae20)
- ブロック [`00bcae20`](#insn-00bcae20) 範囲 `[['00bcae20', '00bcae27']]`
  - `CONDITIONAL_JUMP` [`00bcae24`](#insn-00bcae24) → [`00bcae48`](#insn-00bcae48)
  - `FALL_THROUGH` [`00bcae24`](#insn-00bcae24) → [`00bcae28`](#insn-00bcae28)
- ブロック [`00bcae28`](#insn-00bcae28) 範囲 `[['00bcae28', '00bcae33']]`
  - `CONDITIONAL_JUMP` [`00bcae30`](#insn-00bcae30) → [`00bcae40`](#insn-00bcae40)
  - `FALL_THROUGH` [`00bcae30`](#insn-00bcae30) → [`00bcae34`](#insn-00bcae34)
- ブロック [`00bcae34`](#insn-00bcae34) 範囲 `[['00bcae34', '00bcae3f']]`
  - `FALL_THROUGH` [`00bcae3c`](#insn-00bcae3c) → [`00bcae40`](#insn-00bcae40)
- ブロック [`00bcae40`](#insn-00bcae40) 範囲 `[['00bcae40', '00bcae47']]`
  - `FALL_THROUGH` [`00bcae44`](#insn-00bcae44) → [`00bcae48`](#insn-00bcae48)
- ブロック [`00bcae48`](#insn-00bcae48) 範囲 `[['00bcae48', '00bcae53']]`
  - `CONDITIONAL_JUMP` [`00bcae50`](#insn-00bcae50) → [`00bcaeac`](#insn-00bcaeac)
  - `FALL_THROUGH` [`00bcae50`](#insn-00bcae50) → [`00bcae54`](#insn-00bcae54)
- ブロック [`00bcae54`](#insn-00bcae54) 範囲 `[['00bcae54', '00bcae5f']]`
  - `CONDITIONAL_JUMP` [`00bcae5c`](#insn-00bcae5c) → [`00bcae84`](#insn-00bcae84)
  - `FALL_THROUGH` [`00bcae5c`](#insn-00bcae5c) → [`00bcae60`](#insn-00bcae60)
- ブロック [`00bcae60`](#insn-00bcae60) 範囲 `[['00bcae60', '00bcae67']]`
  - `FALL_THROUGH` [`00bcae64`](#insn-00bcae64) → [`00bcae68`](#insn-00bcae68)
- ブロック [`00bcae68`](#insn-00bcae68) 範囲 `[['00bcae68', '00bcae6b']]`
  - `FALL_THROUGH` [`00bcae68`](#insn-00bcae68) → [`00bcae6c`](#insn-00bcae6c)
- ブロック [`00bcae6c`](#insn-00bcae6c) 範囲 `[['00bcae6c', '00bcae6f']]`
  - `CONDITIONAL_JUMP` [`00bcae6c`](#insn-00bcae6c) → [`00bcaeac`](#insn-00bcaeac)
  - `FALL_THROUGH` [`00bcae6c`](#insn-00bcae6c) → [`00bcae70`](#insn-00bcae70)
- ブロック [`00bcae70`](#insn-00bcae70) 範囲 `[['00bcae70', '00bcae83']]`
  - `CONDITIONAL_JUMP` [`00bcae80`](#insn-00bcae80) → [`00bcae68`](#insn-00bcae68)
  - `FALL_THROUGH` [`00bcae80`](#insn-00bcae80) → [`00bcae84`](#insn-00bcae84)
- ブロック [`00bcae84`](#insn-00bcae84) 範囲 `[['00bcae84', '00bcae8b']]`
  - `CONDITIONAL_JUMP` [`00bcae88`](#insn-00bcae88) → [`00bcaeac`](#insn-00bcaeac)
  - `FALL_THROUGH` [`00bcae88`](#insn-00bcae88) → [`00bcae8c`](#insn-00bcae8c)
- ブロック [`00bcae8c`](#insn-00bcae8c) 範囲 `[['00bcae8c', '00bcae97']]`
  - `CONDITIONAL_JUMP` [`00bcae94`](#insn-00bcae94) → [`00bcaea4`](#insn-00bcaea4)
  - `FALL_THROUGH` [`00bcae94`](#insn-00bcae94) → [`00bcae98`](#insn-00bcae98)
- ブロック [`00bcae98`](#insn-00bcae98) 範囲 `[['00bcae98', '00bcaea3']]`
  - `FALL_THROUGH` [`00bcaea0`](#insn-00bcaea0) → [`00bcaea4`](#insn-00bcaea4)
- ブロック [`00bcaea4`](#insn-00bcaea4) 範囲 `[['00bcaea4', '00bcaeab']]`
  - `FALL_THROUGH` [`00bcaea8`](#insn-00bcaea8) → [`00bcaeac`](#insn-00bcaeac)
- ブロック [`00bcaeac`](#insn-00bcaeac) 範囲 `[['00bcaeac', '00bcaeb3']]`
  - `FALL_THROUGH` [`00bcaeb0`](#insn-00bcaeb0) → [`00bcaeb4`](#insn-00bcaeb4)
- ブロック [`00bcaeb4`](#insn-00bcaeb4) 範囲 `[['00bcaeb4', '00bcaec3']]`

## 命令位置別の参照

- [`00bcadb4`](#insn-00bcadb4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcadb8`](#insn-00bcadb8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcadbc`](#insn-00bcadbc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcadc8`](#insn-00bcadc8) → [`00bcaeb4`](#insn-00bcaeb4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcaddc`](#insn-00bcaddc) → [`00c5a600`](../00c5a/00c5a600.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a600` · 推定シンボル `None` · 推定型 `None`
- [`00bcadec`](#insn-00bcadec) → [`00bcae48`](#insn-00bcae48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcadf8`](#insn-00bcadf8) → [`00bcae20`](#insn-00bcae20) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcae08`](#insn-00bcae08) → [`00bcae48`](#insn-00bcae48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcae1c`](#insn-00bcae1c) → [`00bcae04`](#insn-00bcae04) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcae24`](#insn-00bcae24) → [`00bcae48`](#insn-00bcae48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcae30`](#insn-00bcae30) → [`00bcae40`](#insn-00bcae40) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcae50`](#insn-00bcae50) → [`00bcaeac`](#insn-00bcaeac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcae5c`](#insn-00bcae5c) → [`00bcae84`](#insn-00bcae84) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcae6c`](#insn-00bcae6c) → [`00bcaeac`](#insn-00bcaeac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcae80`](#insn-00bcae80) → [`00bcae68`](#insn-00bcae68) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcae88`](#insn-00bcae88) → [`00bcaeac`](#insn-00bcaeac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcae94`](#insn-00bcae94) → [`00bcaea4`](#insn-00bcaea4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcaeb0`](#insn-00bcaeb0) → [`00c5a610`](../00c5a/00c5a610.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a610` · 推定シンボル `None` · 推定型 `None`
- [`00bcaeb4`](#insn-00bcaeb4) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcaeb8`](#insn-00bcaeb8) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bcadb4`](#insn-00bcadb4)

~~~json
{
  "source": "00bcadb4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcadb8`](#insn-00bcadb8)

~~~json
{
  "source": "00bcadb8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcadbc`](#insn-00bcadbc)

~~~json
{
  "source": "00bcadbc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcadc8`](#insn-00bcadc8)

~~~json
{
  "source": "00bcadc8",
  "target": "00bcaeb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcaddc`](#insn-00bcaddc)

~~~json
{
  "source": "00bcaddc",
  "target": "00c5a600",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcadec`](#insn-00bcadec)

~~~json
{
  "source": "00bcadec",
  "target": "00bcae48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcadf8`](#insn-00bcadf8)

~~~json
{
  "source": "00bcadf8",
  "target": "00bcae20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcae08`](#insn-00bcae08)

~~~json
{
  "source": "00bcae08",
  "target": "00bcae48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcae1c`](#insn-00bcae1c)

~~~json
{
  "source": "00bcae1c",
  "target": "00bcae04",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcae24`](#insn-00bcae24)

~~~json
{
  "source": "00bcae24",
  "target": "00bcae48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcae30`](#insn-00bcae30)

~~~json
{
  "source": "00bcae30",
  "target": "00bcae40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcae50`](#insn-00bcae50)

~~~json
{
  "source": "00bcae50",
  "target": "00bcaeac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcae5c`](#insn-00bcae5c)

~~~json
{
  "source": "00bcae5c",
  "target": "00bcae84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcae6c`](#insn-00bcae6c)

~~~json
{
  "source": "00bcae6c",
  "target": "00bcaeac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcae80`](#insn-00bcae80)

~~~json
{
  "source": "00bcae80",
  "target": "00bcae68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcae88`](#insn-00bcae88)

~~~json
{
  "source": "00bcae88",
  "target": "00bcaeac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcae94`](#insn-00bcae94)

~~~json
{
  "source": "00bcae94",
  "target": "00bcaea4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcaeb0`](#insn-00bcaeb0)

~~~json
{
  "source": "00bcaeb0",
  "target": "00c5a610",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcaeb4`](#insn-00bcaeb4)

~~~json
{
  "source": "00bcaeb4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcaeb8`](#insn-00bcaeb8)

~~~json
{
  "source": "00bcaeb8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
