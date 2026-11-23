# 00adb9dc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00adb914`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00adb/00adb914.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/alignment_unresolved-0001.md#compare-193ef5575f7590fbd1813f085c148a22)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00adba20`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adb/00adba20.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/inspection-0007.md#compare-a67a1c427627250c0d92a6e8175f9478)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00adb9dc",
  "name": "FUN_00adb9dc",
  "size": 260,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "7cdc4072a912f287d5a993e6fac7487fa226f6c14d1ff5d841c709f9a16d0691",
  "source_text_sha256": "7cdc4072a912f287d5a993e6fac7487fa226f6c14d1ff5d841c709f9a16d0691",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00adb9dc",
        "00adbadf"
      ]
    ],
    "bytes_sha256": "5c3e4851a11c271aef661e705f3988e6b248cd5c52db80e216956150be8dfb10",
    "instruction_count": 65,
    "instruction_bytes": 260,
    "body_bytes": 260,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00adacc8](../00ada/00adacc8.md)
- [00adad88](../00ada/00adad88.md)
- [00adae94](../00ada/00adae94.md)

## 呼び出し先

- [00bdb1b0](../00bdb/00bdb1b0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1838 bytes

~~~c

long * FUN_00adb9dc(long param_1,byte *param_2)

{
  void *pvVar1;
  long lVar2;
  ulong uVar3;
  size_t sVar4;
  ulong uVar5;
  byte *__s2;
  bool bVar6;
  int iVar7;
  long *plVar8;
  long *plVar9;
  long *plVar10;
  
                    /* catch() { ... } // from try @ 00adb54c with catch @ 00adb9e4 */
                    /* catch() { ... } // from try @ 00adb53c with catch @ 00adb9e8 */
  plVar8 = (long *)(param_1 + 8);
  plVar10 = (long *)*plVar8;
  if (plVar10 != (long *)0x0) {
    uVar5 = *(ulong *)(param_2 + 8);
    __s2 = *(byte **)(param_2 + 0x10);
    plVar9 = plVar8;
    if ((*param_2 & 1) == 0) {
      __s2 = param_2 + 1;
      uVar5 = (ulong)(*param_2 >> 1);
    }
    do {
      pvVar1 = (void *)((long)plVar10 + 0x21);
      uVar3 = (ulong)(*(byte *)(plVar10 + 4) >> 1);
      if ((*(byte *)(plVar10 + 4) & 1) != 0) {
        pvVar1 = (void *)plVar10[6];
        uVar3 = plVar10[5];
      }
      sVar4 = uVar5;
      if (uVar3 <= uVar5) {
        sVar4 = uVar3;
      }
      iVar7 = memcmp(pvVar1,__s2,sVar4);
      bVar6 = uVar3 < uVar5;
      if (iVar7 != 0) {
        bVar6 = iVar7 < 0;
      }
      lVar2 = 8;
      if (!bVar6) {
        lVar2 = 0;
        plVar9 = plVar10;
      }
      plVar10 = *(long **)((long)plVar10 + lVar2);
    } while (plVar10 != (long *)0x0);
    if (plVar9 != plVar8) {
      uVar3 = (ulong)(*(byte *)(plVar9 + 4) >> 1);
      pvVar1 = (void *)((long)plVar9 + 0x21);
      if ((*(byte *)(plVar9 + 4) & 1) != 0) {
        uVar3 = plVar9[5];
        pvVar1 = (void *)plVar9[6];
      }
      sVar4 = uVar3;
      if (uVar5 <= uVar3) {
        sVar4 = uVar5;
      }
      iVar7 = memcmp(__s2,pvVar1,sVar4);
      bVar6 = uVar5 < uVar3;
      if (iVar7 != 0) {
        bVar6 = iVar7 < 0;
      }
      if (!bVar6) {
        plVar8 = plVar9;
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
<a id="insn-00adb9dc"></a> `00adb9dc` | `fd 7b bb a9` | stp x29,x30,[sp, #-0x50]! | `FALL_THROUGH`
<a id="insn-00adb9e0"></a> `00adb9e0` | `f9 0b 00 f9` | str x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00adb9e4"></a> `00adb9e4` | `f8 5f 02 a9` | stp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00adb9e8"></a> `00adb9e8` | `f6 57 03 a9` | stp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00adb9ec"></a> `00adb9ec` | `f4 4f 04 a9` | stp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00adb9f0"></a> `00adb9f0` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00adb9f4"></a> `00adb9f4` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00adb9f8"></a> `00adb9f8` | `77 8e 40 f8` | ldr x23,[x19, #0x8]! | `FALL_THROUGH`
<a id="insn-00adb9fc"></a> `00adb9fc` | `57 06 00 b4` | cbz x23,0x00adbac4 | `CONDITIONAL_JUMP`
<a id="insn-00adba00"></a> `00adba00` | `28 00 40 39` | ldrb w8,[x1] | `FALL_THROUGH`
<a id="insn-00adba04"></a> `00adba04` | `2a a4 40 a9` | ldp x10,x9,[x1, #0x8] | `FALL_THROUGH`
<a id="insn-00adba08"></a> `00adba08` | `18 01 80 52` | mov w24,#0x8 | `FALL_THROUGH`
<a id="insn-00adba0c"></a> `00adba0c` | `f5 03 13 aa` | mov x21,x19 | `FALL_THROUGH`
<a id="insn-00adba10"></a> `00adba10` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00adba14"></a> `00adba14` | `08 fd 41 d3` | lsr x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00adba18"></a> `00adba18` | `34 15 81 9a` | csinc x20,x9,x1,ne | `FALL_THROUGH`
<a id="insn-00adba1c"></a> `00adba1c` | `16 01 8a 9a` | csel x22,x8,x10,eq | `FALL_THROUGH`
<a id="insn-00adba20"></a> `00adba20` | `e8 82 40 39` | ldrb w8,[x23, #0x20] | `FALL_THROUGH`
<a id="insn-00adba24"></a> `00adba24` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00adba28"></a> `00adba28` | `09 fd 41 d3` | lsr x9,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00adba2c"></a> `00adba2c` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00adba30"></a> `00adba30` | `ea a2 42 a9` | ldp x10,x8,[x23, #0x28] | `FALL_THROUGH`
<a id="insn-00adba34"></a> `00adba34` | `39 01 8a 9a` | csel x25,x9,x10,eq | `FALL_THROUGH`
<a id="insn-00adba38"></a> `00adba38` | `e9 86 00 91` | add x9,x23,#0x21 | `FALL_THROUGH`
<a id="insn-00adba3c"></a> `00adba3c` | `20 01 88 9a` | csel x0,x9,x8,eq | `FALL_THROUGH`
<a id="insn-00adba40"></a> `00adba40` | `df 02 19 eb` | cmp x22,x25 | `FALL_THROUGH`
<a id="insn-00adba44"></a> `00adba44` | `c2 32 99 9a` | csel x2,x22,x25,cc | `FALL_THROUGH`
<a id="insn-00adba48"></a> `00adba48` | `da fd 03 94` | bl 0x00bdb1b0 | `UNCONDITIONAL_CALL`
<a id="insn-00adba4c"></a> `00adba4c` | `3f 03 16 eb` | cmp x25,x22 | `FALL_THROUGH`
<a id="insn-00adba50"></a> `00adba50` | `e8 27 9f 1a` | cset w8,cc | `FALL_THROUGH`
<a id="insn-00adba54"></a> `00adba54` | `1f 00 00 71` | cmp w0,#0x0 | `FALL_THROUGH`
<a id="insn-00adba58"></a> `00adba58` | `e9 a7 9f 1a` | cset w9,lt | `FALL_THROUGH`
<a id="insn-00adba5c"></a> `00adba5c` | `08 01 89 1a` | csel w8,w8,w9,eq | `FALL_THROUGH`
<a id="insn-00adba60"></a> `00adba60` | `1f 01 00 71` | cmp w8,#0x0 | `FALL_THROUGH`
<a id="insn-00adba64"></a> `00adba64` | `08 13 9f 9a` | csel x8,x24,xzr,ne | `FALL_THROUGH`
<a id="insn-00adba68"></a> `00adba68` | `b5 12 97 9a` | csel x21,x21,x23,ne | `FALL_THROUGH`
<a id="insn-00adba6c"></a> `00adba6c` | `f7 6a 68 f8` | ldr x23,[x23, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00adba70"></a> `00adba70` | `97 fd ff b5` | cbnz x23,0x00adba20 | `CONDITIONAL_JUMP`
<a id="insn-00adba74"></a> `00adba74` | `bf 02 13 eb` | cmp x21,x19 | `FALL_THROUGH`
<a id="insn-00adba78"></a> `00adba78` | `60 02 00 54` | b.eq 0x00adbac4 | `CONDITIONAL_JUMP`
<a id="insn-00adba7c"></a> `00adba7c` | `a8 82 40 39` | ldrb w8,[x21, #0x20] | `FALL_THROUGH`
<a id="insn-00adba80"></a> `00adba80` | `a9 ae 42 a9` | ldp x9,x11,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-00adba84"></a> `00adba84` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00adba88"></a> `00adba88` | `0a fd 41 d3` | lsr x10,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00adba8c"></a> `00adba8c` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00adba90"></a> `00adba90` | `a8 86 00 91` | add x8,x21,#0x21 | `FALL_THROUGH`
<a id="insn-00adba94"></a> `00adba94` | `01 01 8b 9a` | csel x1,x8,x11,eq | `FALL_THROUGH`
<a id="insn-00adba98"></a> `00adba98` | `57 01 89 9a` | csel x23,x10,x9,eq | `FALL_THROUGH`
<a id="insn-00adba9c"></a> `00adba9c` | `ff 02 16 eb` | cmp x23,x22 | `FALL_THROUGH`
<a id="insn-00adbaa0"></a> `00adbaa0` | `e2 32 96 9a` | csel x2,x23,x22,cc | `FALL_THROUGH`
<a id="insn-00adbaa4"></a> `00adbaa4` | `c3 fd 03 94` | bl 0x00bdb1b0 | `UNCONDITIONAL_CALL`
<a id="insn-00adbaa8"></a> `00adbaa8` | `df 02 17 eb` | cmp x22,x23 | `FALL_THROUGH`
<a id="insn-00adbaac"></a> `00adbaac` | `e8 27 9f 1a` | cset w8,cc | `FALL_THROUGH`
<a id="insn-00adbab0"></a> `00adbab0` | `1f 00 00 71` | cmp w0,#0x0 | `FALL_THROUGH`
<a id="insn-00adbab4"></a> `00adbab4` | `e9 a7 9f 1a` | cset w9,lt | `FALL_THROUGH`
<a id="insn-00adbab8"></a> `00adbab8` | `08 01 89 1a` | csel w8,w8,w9,eq | `FALL_THROUGH`
<a id="insn-00adbabc"></a> `00adbabc` | `1f 01 00 71` | cmp w8,#0x0 | `FALL_THROUGH`
<a id="insn-00adbac0"></a> `00adbac0` | `73 12 95 9a` | csel x19,x19,x21,ne | `FALL_THROUGH`
<a id="insn-00adbac4"></a> `00adbac4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00adbac8"></a> `00adbac8` | `f4 4f 44 a9` | ldp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00adbacc"></a> `00adbacc` | `f9 0b 40 f9` | ldr x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00adbad0"></a> `00adbad0` | `f6 57 43 a9` | ldp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00adbad4"></a> `00adbad4` | `f8 5f 42 a9` | ldp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00adbad8"></a> `00adbad8` | `fd 7b c5 a8` | ldp x29,x30,[sp], #0x50 | `FALL_THROUGH`
<a id="insn-00adbadc"></a> `00adbadc` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00adb9dc`](#insn-00adb9dc) 範囲 `[['00adb9dc', '00adb9e3']]`
  - `FALL_THROUGH` [`00adb9e0`](#insn-00adb9e0) → [`00adb9e4`](#insn-00adb9e4)
- ブロック [`00adb9e4`](#insn-00adb9e4) 範囲 `[['00adb9e4', '00adb9e7']]`
  - `FALL_THROUGH` [`00adb9e4`](#insn-00adb9e4) → [`00adb9e8`](#insn-00adb9e8)
- ブロック [`00adb9e8`](#insn-00adb9e8) 範囲 `[['00adb9e8', '00adb9ff']]`
  - `CONDITIONAL_JUMP` [`00adb9fc`](#insn-00adb9fc) → [`00adbac4`](#insn-00adbac4)
  - `FALL_THROUGH` [`00adb9fc`](#insn-00adb9fc) → [`00adba00`](#insn-00adba00)
- ブロック [`00adba00`](#insn-00adba00) 範囲 `[['00adba00', '00adba1f']]`
  - `FALL_THROUGH` [`00adba1c`](#insn-00adba1c) → [`00adba20`](#insn-00adba20)
- ブロック [`00adba20`](#insn-00adba20) 範囲 `[['00adba20', '00adba73']]`
  - `CONDITIONAL_JUMP` [`00adba70`](#insn-00adba70) → [`00adba20`](#insn-00adba20)
  - `FALL_THROUGH` [`00adba70`](#insn-00adba70) → [`00adba74`](#insn-00adba74)
- ブロック [`00adba74`](#insn-00adba74) 範囲 `[['00adba74', '00adba7b']]`
  - `CONDITIONAL_JUMP` [`00adba78`](#insn-00adba78) → [`00adbac4`](#insn-00adbac4)
  - `FALL_THROUGH` [`00adba78`](#insn-00adba78) → [`00adba7c`](#insn-00adba7c)
- ブロック [`00adba7c`](#insn-00adba7c) 範囲 `[['00adba7c', '00adbac3']]`
  - `FALL_THROUGH` [`00adbac0`](#insn-00adbac0) → [`00adbac4`](#insn-00adbac4)
- ブロック [`00adbac4`](#insn-00adbac4) 範囲 `[['00adbac4', '00adbadf']]`

## 命令位置別の参照

- [`00adb9dc`](#insn-00adb9dc) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adb9e0`](#insn-00adb9e0) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adb9e4`](#insn-00adb9e4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adb9e8`](#insn-00adb9e8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adb9ec`](#insn-00adb9ec) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adb9fc`](#insn-00adb9fc) → [`00adbac4`](#insn-00adbac4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adba48`](#insn-00adba48) → [`00bdb1b0`](../00bdb/00bdb1b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb1b0` · 推定シンボル `None` · 推定型 `None`
- [`00adba70`](#insn-00adba70) → [`00adba20`](#insn-00adba20) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adba78`](#insn-00adba78) → [`00adbac4`](#insn-00adbac4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbaa4`](#insn-00adbaa4) → [`00bdb1b0`](../00bdb/00bdb1b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb1b0` · 推定シンボル `None` · 推定型 `None`
- [`00adbac8`](#insn-00adbac8) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbacc`](#insn-00adbacc) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbad0`](#insn-00adbad0) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbad4`](#insn-00adbad4) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbad8`](#insn-00adbad8) → `Stack[-0x50]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00adb9dc`](#insn-00adb9dc)

~~~json
{
  "source": "00adb9dc",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adb9e0`](#insn-00adb9e0)

~~~json
{
  "source": "00adb9e0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adb9e4`](#insn-00adb9e4)

~~~json
{
  "source": "00adb9e4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adb9e8`](#insn-00adb9e8)

~~~json
{
  "source": "00adb9e8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adb9ec`](#insn-00adb9ec)

~~~json
{
  "source": "00adb9ec",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adb9fc`](#insn-00adb9fc)

~~~json
{
  "source": "00adb9fc",
  "target": "00adbac4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adba48`](#insn-00adba48)

~~~json
{
  "source": "00adba48",
  "target": "00bdb1b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adba70`](#insn-00adba70)

~~~json
{
  "source": "00adba70",
  "target": "00adba20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adba78`](#insn-00adba78)

~~~json
{
  "source": "00adba78",
  "target": "00adbac4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbaa4`](#insn-00adbaa4)

~~~json
{
  "source": "00adbaa4",
  "target": "00bdb1b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adbac8`](#insn-00adbac8)

~~~json
{
  "source": "00adbac8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbacc`](#insn-00adbacc)

~~~json
{
  "source": "00adbacc",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbad0`](#insn-00adbad0)

~~~json
{
  "source": "00adbad0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbad4`](#insn-00adbad4)

~~~json
{
  "source": "00adbad4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbad8`](#insn-00adbad8)

~~~json
{
  "source": "00adbad8",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
