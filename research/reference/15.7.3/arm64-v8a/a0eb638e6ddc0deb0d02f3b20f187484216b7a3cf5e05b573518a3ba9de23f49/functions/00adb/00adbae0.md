# 00adbae0

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00adba18`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00adb/00adba18.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/inspection-0001.md#compare-cb026748c717b7d4b7c278bc455b7ff9)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00adbb24`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adb/00adbb24.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/inspection-0007.md#compare-dc032cada1fa32174e7da13ebbfad492)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00adbae0",
  "name": "FUN_00adbae0",
  "size": 260,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "7080f1de99dd0ecc88c187f0693d5e23386ea89516badc73f205fb248926e6b4",
  "source_text_sha256": "7080f1de99dd0ecc88c187f0693d5e23386ea89516badc73f205fb248926e6b4",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00adbae0",
        "00adbbe3"
      ]
    ],
    "bytes_sha256": "2e00544988f631ca4c2baa9b3814f6ad6d88f50b2083b9ec8ffec3552691f367",
    "instruction_count": 65,
    "instruction_bytes": 260,
    "body_bytes": 260,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00adaf54](../00ada/00adaf54.md)
- [00adb014](../00adb/00adb014.md)

## 呼び出し先

- [00bdb1b0](../00bdb/00bdb1b0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1664 bytes

~~~c

long * FUN_00adbae0(long param_1,byte *param_2)

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
<a id="insn-00adbae0"></a> `00adbae0` | `fd 7b bb a9` | stp x29,x30,[sp, #-0x50]! | `FALL_THROUGH`
<a id="insn-00adbae4"></a> `00adbae4` | `f9 0b 00 f9` | str x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00adbae8"></a> `00adbae8` | `f8 5f 02 a9` | stp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00adbaec"></a> `00adbaec` | `f6 57 03 a9` | stp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00adbaf0"></a> `00adbaf0` | `f4 4f 04 a9` | stp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00adbaf4"></a> `00adbaf4` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00adbaf8"></a> `00adbaf8` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00adbafc"></a> `00adbafc` | `77 8e 40 f8` | ldr x23,[x19, #0x8]! | `FALL_THROUGH`
<a id="insn-00adbb00"></a> `00adbb00` | `57 06 00 b4` | cbz x23,0x00adbbc8 | `CONDITIONAL_JUMP`
<a id="insn-00adbb04"></a> `00adbb04` | `28 00 40 39` | ldrb w8,[x1] | `FALL_THROUGH`
<a id="insn-00adbb08"></a> `00adbb08` | `2a a4 40 a9` | ldp x10,x9,[x1, #0x8] | `FALL_THROUGH`
<a id="insn-00adbb0c"></a> `00adbb0c` | `18 01 80 52` | mov w24,#0x8 | `FALL_THROUGH`
<a id="insn-00adbb10"></a> `00adbb10` | `f5 03 13 aa` | mov x21,x19 | `FALL_THROUGH`
<a id="insn-00adbb14"></a> `00adbb14` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00adbb18"></a> `00adbb18` | `08 fd 41 d3` | lsr x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00adbb1c"></a> `00adbb1c` | `34 15 81 9a` | csinc x20,x9,x1,ne | `FALL_THROUGH`
<a id="insn-00adbb20"></a> `00adbb20` | `16 01 8a 9a` | csel x22,x8,x10,eq | `FALL_THROUGH`
<a id="insn-00adbb24"></a> `00adbb24` | `e8 82 40 39` | ldrb w8,[x23, #0x20] | `FALL_THROUGH`
<a id="insn-00adbb28"></a> `00adbb28` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00adbb2c"></a> `00adbb2c` | `09 fd 41 d3` | lsr x9,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00adbb30"></a> `00adbb30` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00adbb34"></a> `00adbb34` | `ea a2 42 a9` | ldp x10,x8,[x23, #0x28] | `FALL_THROUGH`
<a id="insn-00adbb38"></a> `00adbb38` | `39 01 8a 9a` | csel x25,x9,x10,eq | `FALL_THROUGH`
<a id="insn-00adbb3c"></a> `00adbb3c` | `e9 86 00 91` | add x9,x23,#0x21 | `FALL_THROUGH`
<a id="insn-00adbb40"></a> `00adbb40` | `20 01 88 9a` | csel x0,x9,x8,eq | `FALL_THROUGH`
<a id="insn-00adbb44"></a> `00adbb44` | `df 02 19 eb` | cmp x22,x25 | `FALL_THROUGH`
<a id="insn-00adbb48"></a> `00adbb48` | `c2 32 99 9a` | csel x2,x22,x25,cc | `FALL_THROUGH`
<a id="insn-00adbb4c"></a> `00adbb4c` | `99 fd 03 94` | bl 0x00bdb1b0 | `UNCONDITIONAL_CALL`
<a id="insn-00adbb50"></a> `00adbb50` | `3f 03 16 eb` | cmp x25,x22 | `FALL_THROUGH`
<a id="insn-00adbb54"></a> `00adbb54` | `e8 27 9f 1a` | cset w8,cc | `FALL_THROUGH`
<a id="insn-00adbb58"></a> `00adbb58` | `1f 00 00 71` | cmp w0,#0x0 | `FALL_THROUGH`
<a id="insn-00adbb5c"></a> `00adbb5c` | `e9 a7 9f 1a` | cset w9,lt | `FALL_THROUGH`
<a id="insn-00adbb60"></a> `00adbb60` | `08 01 89 1a` | csel w8,w8,w9,eq | `FALL_THROUGH`
<a id="insn-00adbb64"></a> `00adbb64` | `1f 01 00 71` | cmp w8,#0x0 | `FALL_THROUGH`
<a id="insn-00adbb68"></a> `00adbb68` | `08 13 9f 9a` | csel x8,x24,xzr,ne | `FALL_THROUGH`
<a id="insn-00adbb6c"></a> `00adbb6c` | `b5 12 97 9a` | csel x21,x21,x23,ne | `FALL_THROUGH`
<a id="insn-00adbb70"></a> `00adbb70` | `f7 6a 68 f8` | ldr x23,[x23, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00adbb74"></a> `00adbb74` | `97 fd ff b5` | cbnz x23,0x00adbb24 | `CONDITIONAL_JUMP`
<a id="insn-00adbb78"></a> `00adbb78` | `bf 02 13 eb` | cmp x21,x19 | `FALL_THROUGH`
<a id="insn-00adbb7c"></a> `00adbb7c` | `60 02 00 54` | b.eq 0x00adbbc8 | `CONDITIONAL_JUMP`
<a id="insn-00adbb80"></a> `00adbb80` | `a8 82 40 39` | ldrb w8,[x21, #0x20] | `FALL_THROUGH`
<a id="insn-00adbb84"></a> `00adbb84` | `a9 ae 42 a9` | ldp x9,x11,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-00adbb88"></a> `00adbb88` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00adbb8c"></a> `00adbb8c` | `0a fd 41 d3` | lsr x10,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00adbb90"></a> `00adbb90` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00adbb94"></a> `00adbb94` | `a8 86 00 91` | add x8,x21,#0x21 | `FALL_THROUGH`
<a id="insn-00adbb98"></a> `00adbb98` | `01 01 8b 9a` | csel x1,x8,x11,eq | `FALL_THROUGH`
<a id="insn-00adbb9c"></a> `00adbb9c` | `57 01 89 9a` | csel x23,x10,x9,eq | `FALL_THROUGH`
<a id="insn-00adbba0"></a> `00adbba0` | `ff 02 16 eb` | cmp x23,x22 | `FALL_THROUGH`
<a id="insn-00adbba4"></a> `00adbba4` | `e2 32 96 9a` | csel x2,x23,x22,cc | `FALL_THROUGH`
<a id="insn-00adbba8"></a> `00adbba8` | `82 fd 03 94` | bl 0x00bdb1b0 | `UNCONDITIONAL_CALL`
<a id="insn-00adbbac"></a> `00adbbac` | `df 02 17 eb` | cmp x22,x23 | `FALL_THROUGH`
<a id="insn-00adbbb0"></a> `00adbbb0` | `e8 27 9f 1a` | cset w8,cc | `FALL_THROUGH`
<a id="insn-00adbbb4"></a> `00adbbb4` | `1f 00 00 71` | cmp w0,#0x0 | `FALL_THROUGH`
<a id="insn-00adbbb8"></a> `00adbbb8` | `e9 a7 9f 1a` | cset w9,lt | `FALL_THROUGH`
<a id="insn-00adbbbc"></a> `00adbbbc` | `08 01 89 1a` | csel w8,w8,w9,eq | `FALL_THROUGH`
<a id="insn-00adbbc0"></a> `00adbbc0` | `1f 01 00 71` | cmp w8,#0x0 | `FALL_THROUGH`
<a id="insn-00adbbc4"></a> `00adbbc4` | `73 12 95 9a` | csel x19,x19,x21,ne | `FALL_THROUGH`
<a id="insn-00adbbc8"></a> `00adbbc8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00adbbcc"></a> `00adbbcc` | `f4 4f 44 a9` | ldp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00adbbd0"></a> `00adbbd0` | `f9 0b 40 f9` | ldr x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00adbbd4"></a> `00adbbd4` | `f6 57 43 a9` | ldp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00adbbd8"></a> `00adbbd8` | `f8 5f 42 a9` | ldp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00adbbdc"></a> `00adbbdc` | `fd 7b c5 a8` | ldp x29,x30,[sp], #0x50 | `FALL_THROUGH`
<a id="insn-00adbbe0"></a> `00adbbe0` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00adbae0`](#insn-00adbae0) 範囲 `[['00adbae0', '00adbb03']]`
  - `CONDITIONAL_JUMP` [`00adbb00`](#insn-00adbb00) → [`00adbbc8`](#insn-00adbbc8)
  - `FALL_THROUGH` [`00adbb00`](#insn-00adbb00) → [`00adbb04`](#insn-00adbb04)
- ブロック [`00adbb04`](#insn-00adbb04) 範囲 `[['00adbb04', '00adbb23']]`
  - `FALL_THROUGH` [`00adbb20`](#insn-00adbb20) → [`00adbb24`](#insn-00adbb24)
- ブロック [`00adbb24`](#insn-00adbb24) 範囲 `[['00adbb24', '00adbb77']]`
  - `CONDITIONAL_JUMP` [`00adbb74`](#insn-00adbb74) → [`00adbb24`](#insn-00adbb24)
  - `FALL_THROUGH` [`00adbb74`](#insn-00adbb74) → [`00adbb78`](#insn-00adbb78)
- ブロック [`00adbb78`](#insn-00adbb78) 範囲 `[['00adbb78', '00adbb7f']]`
  - `CONDITIONAL_JUMP` [`00adbb7c`](#insn-00adbb7c) → [`00adbbc8`](#insn-00adbbc8)
  - `FALL_THROUGH` [`00adbb7c`](#insn-00adbb7c) → [`00adbb80`](#insn-00adbb80)
- ブロック [`00adbb80`](#insn-00adbb80) 範囲 `[['00adbb80', '00adbbc7']]`
  - `FALL_THROUGH` [`00adbbc4`](#insn-00adbbc4) → [`00adbbc8`](#insn-00adbbc8)
- ブロック [`00adbbc8`](#insn-00adbbc8) 範囲 `[['00adbbc8', '00adbbe3']]`

## 命令位置別の参照

- [`00adbae0`](#insn-00adbae0) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbae4`](#insn-00adbae4) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbae8`](#insn-00adbae8) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbaec`](#insn-00adbaec) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbaf0`](#insn-00adbaf0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbb00`](#insn-00adbb00) → [`00adbbc8`](#insn-00adbbc8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbb4c`](#insn-00adbb4c) → [`00bdb1b0`](../00bdb/00bdb1b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb1b0` · 推定シンボル `None` · 推定型 `None`
- [`00adbb74`](#insn-00adbb74) → [`00adbb24`](#insn-00adbb24) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbb7c`](#insn-00adbb7c) → [`00adbbc8`](#insn-00adbbc8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbba8`](#insn-00adbba8) → [`00bdb1b0`](../00bdb/00bdb1b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb1b0` · 推定シンボル `None` · 推定型 `None`
- [`00adbbcc`](#insn-00adbbcc) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbbd0`](#insn-00adbbd0) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbbd4`](#insn-00adbbd4) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbbd8`](#insn-00adbbd8) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adbbdc`](#insn-00adbbdc) → `Stack[-0x50]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00adbae0`](#insn-00adbae0)

~~~json
{
  "source": "00adbae0",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbae4`](#insn-00adbae4)

~~~json
{
  "source": "00adbae4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbae8`](#insn-00adbae8)

~~~json
{
  "source": "00adbae8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbaec`](#insn-00adbaec)

~~~json
{
  "source": "00adbaec",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbaf0`](#insn-00adbaf0)

~~~json
{
  "source": "00adbaf0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbb00`](#insn-00adbb00)

~~~json
{
  "source": "00adbb00",
  "target": "00adbbc8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbb4c`](#insn-00adbb4c)

~~~json
{
  "source": "00adbb4c",
  "target": "00bdb1b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adbb74`](#insn-00adbb74)

~~~json
{
  "source": "00adbb74",
  "target": "00adbb24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbb7c`](#insn-00adbb7c)

~~~json
{
  "source": "00adbb7c",
  "target": "00adbbc8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbba8`](#insn-00adbba8)

~~~json
{
  "source": "00adbba8",
  "target": "00bdb1b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adbbcc`](#insn-00adbbcc)

~~~json
{
  "source": "00adbbcc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbbd0`](#insn-00adbbd0)

~~~json
{
  "source": "00adbbd0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbbd4`](#insn-00adbbd4)

~~~json
{
  "source": "00adbbd4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbbd8`](#insn-00adbbd8)

~~~json
{
  "source": "00adbbd8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adbbdc`](#insn-00adbbdc)

~~~json
{
  "source": "00adbbdc",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
