# 00bcaec8

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b5b9c8`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5b/00b5b9c8.md) · 移動量 `+0x6f500`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0066.md#compare-92fa1dbb95b38d6500c768e9373233a4)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bcb2f0`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcb/00bcb2f0.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0081.md#compare-36bc8cd01574f9ff2afbd2ab2bf76bb2)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bcaec8",
  "name": "_ZN8firebase4auth4Auth21RemoveIdTokenListenerEPNS0_15IdTokenListenerE",
  "size": 344,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "90474be1b35e84cc64e2e4f6f5104a10d80b01d067c9399e3ff2510510fc3f77",
  "source_text_sha256": "90474be1b35e84cc64e2e4f6f5104a10d80b01d067c9399e3ff2510510fc3f77",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bcaec8",
        "00bcb01f"
      ]
    ],
    "bytes_sha256": "62181d4ccecea46c5466619d000752b803c011bf9da908226ab4df7994de6e9e",
    "instruction_count": 86,
    "instruction_bytes": 344,
    "body_bytes": 344,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c5d660](../00c5d/00c5d660.md)

## 呼び出し先

- [00c5a600](../00c5a/00c5a600.md)
- [00c5a610](../00c5a/00c5a610.md)
- [00c5d600](../00c5d/00c5d600.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 3383 bytes

~~~c

void _ZN8firebase4auth4Auth21RemoveIdTokenListenerEPNS0_15IdTokenListenerE
               (long *param_1,long param_2)

{
  long *plVar1;
  undefined8 *puVar2;
  long *plVar3;
  undefined8 *puVar4;
  long *plVar5;
  undefined8 *puVar6;
  long lVar7;
  long lVar8;
  long lVar9;
  
                    /* try { // try from 00bcaed0 to 00ccaedb has its CatchHandler @ 00bcafd0 */
                    /* try { // try from 00bcaedc to 00ccaeff has its CatchHandler @ 00bcae6c */
  lVar9 = *param_1;
  if (lVar9 != 0) {
    lVar7 = *(long *)(lVar9 + 0x250);
    lVar8 = *(long *)(lVar9 + 0x248);
    _ZN8firebase5Mutex7AcquireEv(lVar9 + 0x268);
                    /* try { // try from 00bcaf00 to 00ccaf0b has its CatchHandler @ 00bcafd0 */
    plVar5 = *(long **)(lVar9 + 0x248);
    plVar3 = *(long **)(lVar9 + 0x250);
                    /* try { // try from 00bcaf0c to 00ccaf33 has its CatchHandler @ 00bcae6c */
    if (plVar3 != plVar5) {
      if (*plVar5 != param_2) {
        do {
          if (plVar3 + -1 == plVar5) goto LAB_00bcaf68;
          plVar1 = plVar5 + 1;
          plVar5 = plVar5 + 1;
                    /* try { // try from 00bcaf34 to 00ccaf3f has its CatchHandler @ 00bcafd0 */
        } while (*plVar1 != param_2);
      }
                    /* try { // try from 00bcaf40 to 00ccaf5f has its CatchHandler @ 00bcae6c */
      if (plVar5 != plVar3) {
        if (plVar3 + -1 != plVar5) {
          *plVar5 = plVar3[-1];
          plVar3 = *(long **)(lVar9 + 0x250);
        }
                    /* try { // try from 00bcaf60 to 00ccaf67 has its CatchHandler @ 00bcafd0 */
        *(long **)(lVar9 + 0x250) = plVar3 + -1;
      }
    }
LAB_00bcaf68:
                    /* try { // try from 00bcaf68 to 00ccaf87 has its CatchHandler @ 00bcae6c */
    puVar6 = *(undefined8 **)(param_2 + 8);
    puVar4 = *(undefined8 **)(param_2 + 0x10);
    if (puVar4 != puVar6) {
      if ((long *)*puVar6 != param_1) {
        do {
                    /* try { // try from 00bcaf88 to 00ccaf93 has its CatchHandler @ 00bcafd0 */
          if (puVar4 + -1 == puVar6) goto LAB_00bcafcc;
          puVar2 = puVar6 + 1;
                    /* try { // try from 00bcaf94 to 00ccafd3 has its CatchHandler @ 00bcae6c */
          puVar6 = puVar6 + 1;
        } while ((long *)*puVar2 != param_1);
      }
      if (puVar6 != puVar4) {
        if (puVar4 + -1 != puVar6) {
          *puVar6 = puVar4[-1];
          puVar4 = *(undefined8 **)(param_2 + 0x10);
        }
        *(undefined8 **)(param_2 + 0x10) = puVar4 + -1;
      }
    }
LAB_00bcafcc:
                    /* catch(type#1 @ 00000000) { ... } // from try @ 00bcaed0 with catch @ 00bcafd0
                       catch(type#1 @ 00000000) { ... } // from try @ 00bcaf00 with catch @ 00bcafd0
                       catch(type#1 @ 00000000) { ... } // from try @ 00bcaf34 with catch @ 00bcafd0
                       catch(type#1 @ 00000000) { ... } // from try @ 00bcaf60 with catch @ 00bcafd0
                       catch(type#1 @ 00000000) { ... } // from try @ 00bcaf88 with catch @ 00bcafd0
                        */
    _ZN8firebase5Mutex7ReleaseEv(lVar9 + 0x268);
    if ((ulong)(*(long *)(*param_1 + 0x250) - *(long *)(*param_1 + 0x248) >> 3) <
        (ulong)(long)(int)((ulong)(lVar7 - lVar8) >> 3)) {
      _ZN8firebase4auth23DisableTokenAutoRefreshEPNS0_8AuthDataE();
      return;
    }
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bcaec8"></a> `00bcaec8` | `f8 5f bc a9` | stp x24,x23,[sp, #-0x40]! | `FALL_THROUGH`
<a id="insn-00bcaecc"></a> `00bcaecc` | `f6 57 01 a9` | stp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcaed0"></a> `00bcaed0` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcaed4"></a> `00bcaed4` | `fd 7b 03 a9` | stp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bcaed8"></a> `00bcaed8` | `fd c3 00 91` | add x29,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00bcaedc"></a> `00bcaedc` | `18 00 40 f9` | ldr x24,[x0] | `FALL_THROUGH`
<a id="insn-00bcaee0"></a> `00bcaee0` | `78 09 00 b4` | cbz x24,0x00bcb00c | `CONDITIONAL_JUMP`
<a id="insn-00bcaee4"></a> `00bcaee4` | `16 2b 41 f9` | ldr x22,[x24, #0x250] | `FALL_THROUGH`
<a id="insn-00bcaee8"></a> `00bcaee8` | `17 27 41 f9` | ldr x23,[x24, #0x248] | `FALL_THROUGH`
<a id="insn-00bcaeec"></a> `00bcaeec` | `15 a3 09 91` | add x21,x24,#0x268 | `FALL_THROUGH`
<a id="insn-00bcaef0"></a> `00bcaef0` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bcaef4"></a> `00bcaef4` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bcaef8"></a> `00bcaef8` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-00bcaefc"></a> `00bcaefc` | `c1 3d 02 94` | bl 0x00c5a600 | `UNCONDITIONAL_CALL`
<a id="insn-00bcaf00"></a> `00bcaf00` | `09 27 41 f9` | ldr x9,[x24, #0x248] | `FALL_THROUGH`
<a id="insn-00bcaf04"></a> `00bcaf04` | `08 2b 41 f9` | ldr x8,[x24, #0x250] | `FALL_THROUGH`
<a id="insn-00bcaf08"></a> `00bcaf08` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bcaf0c"></a> `00bcaf0c` | `e0 02 00 54` | b.eq 0x00bcaf68 | `CONDITIONAL_JUMP`
<a id="insn-00bcaf10"></a> `00bcaf10` | `2a 01 40 f9` | ldr x10,[x9] | `FALL_THROUGH`
<a id="insn-00bcaf14"></a> `00bcaf14` | `5f 01 14 eb` | cmp x10,x20 | `FALL_THROUGH`
<a id="insn-00bcaf18"></a> `00bcaf18` | `40 01 00 54` | b.eq 0x00bcaf40 | `CONDITIONAL_JUMP`
<a id="insn-00bcaf1c"></a> `00bcaf1c` | `0a 21 00 d1` | sub x10,x8,#0x8 | `FALL_THROUGH`
<a id="insn-00bcaf20"></a> `00bcaf20` | `eb 03 09 aa` | mov x11,x9 | `FALL_THROUGH`
<a id="insn-00bcaf24"></a> `00bcaf24` | `5f 01 0b eb` | cmp x10,x11 | `FALL_THROUGH`
<a id="insn-00bcaf28"></a> `00bcaf28` | `00 02 00 54` | b.eq 0x00bcaf68 | `CONDITIONAL_JUMP`
<a id="insn-00bcaf2c"></a> `00bcaf2c` | `6c 05 40 f9` | ldr x12,[x11, #0x8] | `FALL_THROUGH`
<a id="insn-00bcaf30"></a> `00bcaf30` | `69 21 00 91` | add x9,x11,#0x8 | `FALL_THROUGH`
<a id="insn-00bcaf34"></a> `00bcaf34` | `eb 03 09 aa` | mov x11,x9 | `FALL_THROUGH`
<a id="insn-00bcaf38"></a> `00bcaf38` | `9f 01 14 eb` | cmp x12,x20 | `FALL_THROUGH`
<a id="insn-00bcaf3c"></a> `00bcaf3c` | `41 ff ff 54` | b.ne 0x00bcaf24 | `CONDITIONAL_JUMP`
<a id="insn-00bcaf40"></a> `00bcaf40` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bcaf44"></a> `00bcaf44` | `20 01 00 54` | b.eq 0x00bcaf68 | `CONDITIONAL_JUMP`
<a id="insn-00bcaf48"></a> `00bcaf48` | `0a 21 00 d1` | sub x10,x8,#0x8 | `FALL_THROUGH`
<a id="insn-00bcaf4c"></a> `00bcaf4c` | `5f 01 09 eb` | cmp x10,x9 | `FALL_THROUGH`
<a id="insn-00bcaf50"></a> `00bcaf50` | `80 00 00 54` | b.eq 0x00bcaf60 | `CONDITIONAL_JUMP`
<a id="insn-00bcaf54"></a> `00bcaf54` | `48 01 40 f9` | ldr x8,[x10] | `FALL_THROUGH`
<a id="insn-00bcaf58"></a> `00bcaf58` | `28 01 00 f9` | str x8,[x9] | `FALL_THROUGH`
<a id="insn-00bcaf5c"></a> `00bcaf5c` | `08 2b 41 f9` | ldr x8,[x24, #0x250] | `FALL_THROUGH`
<a id="insn-00bcaf60"></a> `00bcaf60` | `08 21 00 d1` | sub x8,x8,#0x8 | `FALL_THROUGH`
<a id="insn-00bcaf64"></a> `00bcaf64` | `08 2b 01 f9` | str x8,[x24, #0x250] | `FALL_THROUGH`
<a id="insn-00bcaf68"></a> `00bcaf68` | `89 a2 40 a9` | ldp x9,x8,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00bcaf6c"></a> `00bcaf6c` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bcaf70"></a> `00bcaf70` | `e0 02 00 54` | b.eq 0x00bcafcc | `CONDITIONAL_JUMP`
<a id="insn-00bcaf74"></a> `00bcaf74` | `2a 01 40 f9` | ldr x10,[x9] | `FALL_THROUGH`
<a id="insn-00bcaf78"></a> `00bcaf78` | `5f 01 13 eb` | cmp x10,x19 | `FALL_THROUGH`
<a id="insn-00bcaf7c"></a> `00bcaf7c` | `40 01 00 54` | b.eq 0x00bcafa4 | `CONDITIONAL_JUMP`
<a id="insn-00bcaf80"></a> `00bcaf80` | `0a 21 00 d1` | sub x10,x8,#0x8 | `FALL_THROUGH`
<a id="insn-00bcaf84"></a> `00bcaf84` | `eb 03 09 aa` | mov x11,x9 | `FALL_THROUGH`
<a id="insn-00bcaf88"></a> `00bcaf88` | `5f 01 0b eb` | cmp x10,x11 | `FALL_THROUGH`
<a id="insn-00bcaf8c"></a> `00bcaf8c` | `00 02 00 54` | b.eq 0x00bcafcc | `CONDITIONAL_JUMP`
<a id="insn-00bcaf90"></a> `00bcaf90` | `6c 05 40 f9` | ldr x12,[x11, #0x8] | `FALL_THROUGH`
<a id="insn-00bcaf94"></a> `00bcaf94` | `69 21 00 91` | add x9,x11,#0x8 | `FALL_THROUGH`
<a id="insn-00bcaf98"></a> `00bcaf98` | `eb 03 09 aa` | mov x11,x9 | `FALL_THROUGH`
<a id="insn-00bcaf9c"></a> `00bcaf9c` | `9f 01 13 eb` | cmp x12,x19 | `FALL_THROUGH`
<a id="insn-00bcafa0"></a> `00bcafa0` | `41 ff ff 54` | b.ne 0x00bcaf88 | `CONDITIONAL_JUMP`
<a id="insn-00bcafa4"></a> `00bcafa4` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bcafa8"></a> `00bcafa8` | `20 01 00 54` | b.eq 0x00bcafcc | `CONDITIONAL_JUMP`
<a id="insn-00bcafac"></a> `00bcafac` | `0a 21 00 d1` | sub x10,x8,#0x8 | `FALL_THROUGH`
<a id="insn-00bcafb0"></a> `00bcafb0` | `5f 01 09 eb` | cmp x10,x9 | `FALL_THROUGH`
<a id="insn-00bcafb4"></a> `00bcafb4` | `80 00 00 54` | b.eq 0x00bcafc4 | `CONDITIONAL_JUMP`
<a id="insn-00bcafb8"></a> `00bcafb8` | `48 01 40 f9` | ldr x8,[x10] | `FALL_THROUGH`
<a id="insn-00bcafbc"></a> `00bcafbc` | `28 01 00 f9` | str x8,[x9] | `FALL_THROUGH`
<a id="insn-00bcafc0"></a> `00bcafc0` | `88 0a 40 f9` | ldr x8,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-00bcafc4"></a> `00bcafc4` | `08 21 00 d1` | sub x8,x8,#0x8 | `FALL_THROUGH`
<a id="insn-00bcafc8"></a> `00bcafc8` | `88 0a 00 f9` | str x8,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-00bcafcc"></a> `00bcafcc` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bcafd0"></a> `00bcafd0` | `90 3d 02 94` | bl 0x00c5a610 | `UNCONDITIONAL_CALL`
<a id="insn-00bcafd4"></a> `00bcafd4` | `60 02 40 f9` | ldr x0,[x19] | `FALL_THROUGH`
<a id="insn-00bcafd8"></a> `00bcafd8` | `ca 02 17 cb` | sub x10,x22,x23 | `FALL_THROUGH`
<a id="insn-00bcafdc"></a> `00bcafdc` | `08 28 41 f9` | ldr x8,[x0, #0x250] | `FALL_THROUGH`
<a id="insn-00bcafe0"></a> `00bcafe0` | `09 24 41 f9` | ldr x9,[x0, #0x248] | `FALL_THROUGH`
<a id="insn-00bcafe4"></a> `00bcafe4` | `08 01 09 cb` | sub x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00bcafe8"></a> `00bcafe8` | `08 fd 43 93` | asr x8,x8,#0x3 | `FALL_THROUGH`
<a id="insn-00bcafec"></a> `00bcafec` | `49 fd 43 d3` | lsr x9,x10,#0x3 | `FALL_THROUGH`
<a id="insn-00bcaff0"></a> `00bcaff0` | `1f c1 29 eb` | cmp x8,w9, SXTW  | `FALL_THROUGH`
<a id="insn-00bcaff4"></a> `00bcaff4` | `c2 00 00 54` | b.cs 0x00bcb00c | `CONDITIONAL_JUMP`
<a id="insn-00bcaff8"></a> `00bcaff8` | `fd 7b 43 a9` | ldp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bcaffc"></a> `00bcaffc` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcb000"></a> `00bcb000` | `f6 57 41 a9` | ldp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcb004"></a> `00bcb004` | `f8 5f c4 a8` | ldp x24,x23,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-00bcb008"></a> `00bcb008` | `7e 49 02 14` | b 0x00c5d600 | `CALL_TERMINATOR`
<a id="insn-00bcb00c"></a> `00bcb00c` | `fd 7b 43 a9` | ldp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bcb010"></a> `00bcb010` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcb014"></a> `00bcb014` | `f6 57 41 a9` | ldp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcb018"></a> `00bcb018` | `f8 5f c4 a8` | ldp x24,x23,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-00bcb01c"></a> `00bcb01c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bcaec8`](#insn-00bcaec8) 範囲 `[['00bcaec8', '00bcaecf']]`
  - `FALL_THROUGH` [`00bcaecc`](#insn-00bcaecc) → [`00bcaed0`](#insn-00bcaed0)
- ブロック [`00bcaed0`](#insn-00bcaed0) 範囲 `[['00bcaed0', '00bcaedb']]`
  - `FALL_THROUGH` [`00bcaed8`](#insn-00bcaed8) → [`00bcaedc`](#insn-00bcaedc)
- ブロック [`00bcaedc`](#insn-00bcaedc) 範囲 `[['00bcaedc', '00bcaee3']]`
  - `CONDITIONAL_JUMP` [`00bcaee0`](#insn-00bcaee0) → [`00bcb00c`](#insn-00bcb00c)
  - `FALL_THROUGH` [`00bcaee0`](#insn-00bcaee0) → [`00bcaee4`](#insn-00bcaee4)
- ブロック [`00bcaee4`](#insn-00bcaee4) 範囲 `[['00bcaee4', '00bcaeff']]`
  - `FALL_THROUGH` [`00bcaefc`](#insn-00bcaefc) → [`00bcaf00`](#insn-00bcaf00)
- ブロック [`00bcaf00`](#insn-00bcaf00) 範囲 `[['00bcaf00', '00bcaf0b']]`
  - `FALL_THROUGH` [`00bcaf08`](#insn-00bcaf08) → [`00bcaf0c`](#insn-00bcaf0c)
- ブロック [`00bcaf0c`](#insn-00bcaf0c) 範囲 `[['00bcaf0c', '00bcaf0f']]`
  - `CONDITIONAL_JUMP` [`00bcaf0c`](#insn-00bcaf0c) → [`00bcaf68`](#insn-00bcaf68)
  - `FALL_THROUGH` [`00bcaf0c`](#insn-00bcaf0c) → [`00bcaf10`](#insn-00bcaf10)
- ブロック [`00bcaf10`](#insn-00bcaf10) 範囲 `[['00bcaf10', '00bcaf1b']]`
  - `CONDITIONAL_JUMP` [`00bcaf18`](#insn-00bcaf18) → [`00bcaf40`](#insn-00bcaf40)
  - `FALL_THROUGH` [`00bcaf18`](#insn-00bcaf18) → [`00bcaf1c`](#insn-00bcaf1c)
- ブロック [`00bcaf1c`](#insn-00bcaf1c) 範囲 `[['00bcaf1c', '00bcaf23']]`
  - `FALL_THROUGH` [`00bcaf20`](#insn-00bcaf20) → [`00bcaf24`](#insn-00bcaf24)
- ブロック [`00bcaf24`](#insn-00bcaf24) 範囲 `[['00bcaf24', '00bcaf2b']]`
  - `CONDITIONAL_JUMP` [`00bcaf28`](#insn-00bcaf28) → [`00bcaf68`](#insn-00bcaf68)
  - `FALL_THROUGH` [`00bcaf28`](#insn-00bcaf28) → [`00bcaf2c`](#insn-00bcaf2c)
- ブロック [`00bcaf2c`](#insn-00bcaf2c) 範囲 `[['00bcaf2c', '00bcaf33']]`
  - `FALL_THROUGH` [`00bcaf30`](#insn-00bcaf30) → [`00bcaf34`](#insn-00bcaf34)
- ブロック [`00bcaf34`](#insn-00bcaf34) 範囲 `[['00bcaf34', '00bcaf3f']]`
  - `CONDITIONAL_JUMP` [`00bcaf3c`](#insn-00bcaf3c) → [`00bcaf24`](#insn-00bcaf24)
  - `FALL_THROUGH` [`00bcaf3c`](#insn-00bcaf3c) → [`00bcaf40`](#insn-00bcaf40)
- ブロック [`00bcaf40`](#insn-00bcaf40) 範囲 `[['00bcaf40', '00bcaf47']]`
  - `CONDITIONAL_JUMP` [`00bcaf44`](#insn-00bcaf44) → [`00bcaf68`](#insn-00bcaf68)
  - `FALL_THROUGH` [`00bcaf44`](#insn-00bcaf44) → [`00bcaf48`](#insn-00bcaf48)
- ブロック [`00bcaf48`](#insn-00bcaf48) 範囲 `[['00bcaf48', '00bcaf53']]`
  - `CONDITIONAL_JUMP` [`00bcaf50`](#insn-00bcaf50) → [`00bcaf60`](#insn-00bcaf60)
  - `FALL_THROUGH` [`00bcaf50`](#insn-00bcaf50) → [`00bcaf54`](#insn-00bcaf54)
- ブロック [`00bcaf54`](#insn-00bcaf54) 範囲 `[['00bcaf54', '00bcaf5f']]`
  - `FALL_THROUGH` [`00bcaf5c`](#insn-00bcaf5c) → [`00bcaf60`](#insn-00bcaf60)
- ブロック [`00bcaf60`](#insn-00bcaf60) 範囲 `[['00bcaf60', '00bcaf67']]`
  - `FALL_THROUGH` [`00bcaf64`](#insn-00bcaf64) → [`00bcaf68`](#insn-00bcaf68)
- ブロック [`00bcaf68`](#insn-00bcaf68) 範囲 `[['00bcaf68', '00bcaf73']]`
  - `CONDITIONAL_JUMP` [`00bcaf70`](#insn-00bcaf70) → [`00bcafcc`](#insn-00bcafcc)
  - `FALL_THROUGH` [`00bcaf70`](#insn-00bcaf70) → [`00bcaf74`](#insn-00bcaf74)
- ブロック [`00bcaf74`](#insn-00bcaf74) 範囲 `[['00bcaf74', '00bcaf7f']]`
  - `CONDITIONAL_JUMP` [`00bcaf7c`](#insn-00bcaf7c) → [`00bcafa4`](#insn-00bcafa4)
  - `FALL_THROUGH` [`00bcaf7c`](#insn-00bcaf7c) → [`00bcaf80`](#insn-00bcaf80)
- ブロック [`00bcaf80`](#insn-00bcaf80) 範囲 `[['00bcaf80', '00bcaf87']]`
  - `FALL_THROUGH` [`00bcaf84`](#insn-00bcaf84) → [`00bcaf88`](#insn-00bcaf88)
- ブロック [`00bcaf88`](#insn-00bcaf88) 範囲 `[['00bcaf88', '00bcaf8f']]`
  - `CONDITIONAL_JUMP` [`00bcaf8c`](#insn-00bcaf8c) → [`00bcafcc`](#insn-00bcafcc)
  - `FALL_THROUGH` [`00bcaf8c`](#insn-00bcaf8c) → [`00bcaf90`](#insn-00bcaf90)
- ブロック [`00bcaf90`](#insn-00bcaf90) 範囲 `[['00bcaf90', '00bcaf93']]`
  - `FALL_THROUGH` [`00bcaf90`](#insn-00bcaf90) → [`00bcaf94`](#insn-00bcaf94)
- ブロック [`00bcaf94`](#insn-00bcaf94) 範囲 `[['00bcaf94', '00bcafa3']]`
  - `CONDITIONAL_JUMP` [`00bcafa0`](#insn-00bcafa0) → [`00bcaf88`](#insn-00bcaf88)
  - `FALL_THROUGH` [`00bcafa0`](#insn-00bcafa0) → [`00bcafa4`](#insn-00bcafa4)
- ブロック [`00bcafa4`](#insn-00bcafa4) 範囲 `[['00bcafa4', '00bcafab']]`
  - `CONDITIONAL_JUMP` [`00bcafa8`](#insn-00bcafa8) → [`00bcafcc`](#insn-00bcafcc)
  - `FALL_THROUGH` [`00bcafa8`](#insn-00bcafa8) → [`00bcafac`](#insn-00bcafac)
- ブロック [`00bcafac`](#insn-00bcafac) 範囲 `[['00bcafac', '00bcafb7']]`
  - `CONDITIONAL_JUMP` [`00bcafb4`](#insn-00bcafb4) → [`00bcafc4`](#insn-00bcafc4)
  - `FALL_THROUGH` [`00bcafb4`](#insn-00bcafb4) → [`00bcafb8`](#insn-00bcafb8)
- ブロック [`00bcafb8`](#insn-00bcafb8) 範囲 `[['00bcafb8', '00bcafc3']]`
  - `FALL_THROUGH` [`00bcafc0`](#insn-00bcafc0) → [`00bcafc4`](#insn-00bcafc4)
- ブロック [`00bcafc4`](#insn-00bcafc4) 範囲 `[['00bcafc4', '00bcafcb']]`
  - `FALL_THROUGH` [`00bcafc8`](#insn-00bcafc8) → [`00bcafcc`](#insn-00bcafcc)
- ブロック [`00bcafcc`](#insn-00bcafcc) 範囲 `[['00bcafcc', '00bcafcf']]`
  - `FALL_THROUGH` [`00bcafcc`](#insn-00bcafcc) → [`00bcafd0`](#insn-00bcafd0)
- ブロック [`00bcafd0`](#insn-00bcafd0) 範囲 `[['00bcafd0', '00bcaff7']]`
  - `CONDITIONAL_JUMP` [`00bcaff4`](#insn-00bcaff4) → [`00bcb00c`](#insn-00bcb00c)
  - `FALL_THROUGH` [`00bcaff4`](#insn-00bcaff4) → [`00bcaff8`](#insn-00bcaff8)
- ブロック [`00bcaff8`](#insn-00bcaff8) 範囲 `[['00bcaff8', '00bcb00b']]`
- ブロック [`00bcb00c`](#insn-00bcb00c) 範囲 `[['00bcb00c', '00bcb01f']]`

## 命令位置別の参照

- [`00bcaec8`](#insn-00bcaec8) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcaecc`](#insn-00bcaecc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcaed0`](#insn-00bcaed0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcaed4`](#insn-00bcaed4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcaee0`](#insn-00bcaee0) → [`00bcb00c`](#insn-00bcb00c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcaefc`](#insn-00bcaefc) → [`00c5a600`](../00c5a/00c5a600.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a600` · 推定シンボル `None` · 推定型 `None`
- [`00bcaf0c`](#insn-00bcaf0c) → [`00bcaf68`](#insn-00bcaf68) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcaf18`](#insn-00bcaf18) → [`00bcaf40`](#insn-00bcaf40) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcaf28`](#insn-00bcaf28) → [`00bcaf68`](#insn-00bcaf68) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcaf3c`](#insn-00bcaf3c) → [`00bcaf24`](#insn-00bcaf24) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcaf44`](#insn-00bcaf44) → [`00bcaf68`](#insn-00bcaf68) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcaf50`](#insn-00bcaf50) → [`00bcaf60`](#insn-00bcaf60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcaf70`](#insn-00bcaf70) → [`00bcafcc`](#insn-00bcafcc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcaf7c`](#insn-00bcaf7c) → [`00bcafa4`](#insn-00bcafa4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcaf8c`](#insn-00bcaf8c) → [`00bcafcc`](#insn-00bcafcc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcafa0`](#insn-00bcafa0) → [`00bcaf88`](#insn-00bcaf88) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcafa8`](#insn-00bcafa8) → [`00bcafcc`](#insn-00bcafcc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcafb4`](#insn-00bcafb4) → [`00bcafc4`](#insn-00bcafc4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcafd0`](#insn-00bcafd0) → [`00c5a610`](../00c5a/00c5a610.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a610` · 推定シンボル `None` · 推定型 `None`
- [`00bcaff4`](#insn-00bcaff4) → [`00bcb00c`](#insn-00bcb00c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcaff8`](#insn-00bcaff8) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcaffc`](#insn-00bcaffc) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcb000`](#insn-00bcb000) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcb008`](#insn-00bcb008) → [`00c5d600`](../00c5d/00c5d600.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5d600` · 推定シンボル `None` · 推定型 `None`
- [`00bcb00c`](#insn-00bcb00c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcb010`](#insn-00bcb010) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcb014`](#insn-00bcb014) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bcaec8`](#insn-00bcaec8)

~~~json
{
  "source": "00bcaec8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcaecc`](#insn-00bcaecc)

~~~json
{
  "source": "00bcaecc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcaed0`](#insn-00bcaed0)

~~~json
{
  "source": "00bcaed0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcaed4`](#insn-00bcaed4)

~~~json
{
  "source": "00bcaed4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcaee0`](#insn-00bcaee0)

~~~json
{
  "source": "00bcaee0",
  "target": "00bcb00c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcaefc`](#insn-00bcaefc)

~~~json
{
  "source": "00bcaefc",
  "target": "00c5a600",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcaf0c`](#insn-00bcaf0c)

~~~json
{
  "source": "00bcaf0c",
  "target": "00bcaf68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcaf18`](#insn-00bcaf18)

~~~json
{
  "source": "00bcaf18",
  "target": "00bcaf40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcaf28`](#insn-00bcaf28)

~~~json
{
  "source": "00bcaf28",
  "target": "00bcaf68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcaf3c`](#insn-00bcaf3c)

~~~json
{
  "source": "00bcaf3c",
  "target": "00bcaf24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcaf44`](#insn-00bcaf44)

~~~json
{
  "source": "00bcaf44",
  "target": "00bcaf68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcaf50`](#insn-00bcaf50)

~~~json
{
  "source": "00bcaf50",
  "target": "00bcaf60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcaf70`](#insn-00bcaf70)

~~~json
{
  "source": "00bcaf70",
  "target": "00bcafcc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcaf7c`](#insn-00bcaf7c)

~~~json
{
  "source": "00bcaf7c",
  "target": "00bcafa4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcaf8c`](#insn-00bcaf8c)

~~~json
{
  "source": "00bcaf8c",
  "target": "00bcafcc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcafa0`](#insn-00bcafa0)

~~~json
{
  "source": "00bcafa0",
  "target": "00bcaf88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcafa8`](#insn-00bcafa8)

~~~json
{
  "source": "00bcafa8",
  "target": "00bcafcc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcafb4`](#insn-00bcafb4)

~~~json
{
  "source": "00bcafb4",
  "target": "00bcafc4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcafd0`](#insn-00bcafd0)

~~~json
{
  "source": "00bcafd0",
  "target": "00c5a610",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcaff4`](#insn-00bcaff4)

~~~json
{
  "source": "00bcaff4",
  "target": "00bcb00c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcaff8`](#insn-00bcaff8)

~~~json
{
  "source": "00bcaff8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcaffc`](#insn-00bcaffc)

~~~json
{
  "source": "00bcaffc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcb000`](#insn-00bcb000)

~~~json
{
  "source": "00bcb000",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcb008`](#insn-00bcb008)

~~~json
{
  "source": "00bcb008",
  "target": "00c5d600",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcb00c`](#insn-00bcb00c)

~~~json
{
  "source": "00bcb00c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcb010`](#insn-00bcb010)

~~~json
{
  "source": "00bcb010",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcb014`](#insn-00bcb014)

~~~json
{
  "source": "00bcb014",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
