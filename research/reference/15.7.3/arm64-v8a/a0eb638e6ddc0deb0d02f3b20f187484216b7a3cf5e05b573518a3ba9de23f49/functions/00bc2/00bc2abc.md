# 00bc2abc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bc29f4`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc2/00bc29f4.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/inspection-0007.md#compare-3e6db59a8ddf89d0b4abda4077543ae2)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bc2b00`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc2b00.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/inspection-0018.md#compare-293a879bdad9728916240131e9ef5bea)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bc2abc",
  "name": "FUN_00bc2abc",
  "size": 216,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f41ea8e166ba40514916ae52fb45e512916f7efff04fcdb0855b1b70e445a031",
  "source_text_sha256": "f41ea8e166ba40514916ae52fb45e512916f7efff04fcdb0855b1b70e445a031",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bc2abc",
        "00bc2b93"
      ]
    ],
    "bytes_sha256": "1bb8add89d383353382d3cd2346e6f11a0d8503ab6ede9158338913817377664",
    "instruction_count": 54,
    "instruction_bytes": 216,
    "body_bytes": 216,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00bc1c88](../00bc1/00bc1c88.md)

## 呼び出し先

- [00bdb0a0](../00bdb/00bdb0a0.md)
- [00bdd180](../00bdd/00bdd180.md)
- [00bdd200](../00bdd/00bdd200.md)
- [00bde270](../00bde/00bde270.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1124 bytes

~~~c

void FUN_00bc2abc(undefined8 *param_1,undefined8 *param_2)

{
  void *__dest;
  undefined8 uVar1;
  size_t __n;
  undefined8 *__src;
  undefined8 *puVar2;
  
  puVar2 = (undefined8 *)param_1[1];
  if (puVar2 == (undefined8 *)param_1[2]) {
    __src = (undefined8 *)*param_1;
    __n = (long)puVar2 - (long)__src;
    if (__src == param_1 + 3) {
      __dest = malloc(__n * 2);
      if (__dest == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
        abort();
      }
      if (puVar2 != __src) {
        memmove(__dest,__src,__n);
      }
      *param_1 = __dest;
    }
    else {
      __dest = realloc(__src,__n * 2);
      *param_1 = __dest;
      if (__dest == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
        abort();
      }
    }
    puVar2 = (undefined8 *)((long)__dest + __n);
    param_1[1] = puVar2;
    param_1[2] = (void *)((long)__dest + ((long)__n >> 2) * 8);
  }
  uVar1 = *param_2;
  param_1[1] = puVar2 + 1;
  *puVar2 = uVar1;
                    /* try { // try from 00bc2b7c to 00cc2ba7 has its CatchHandler @ 00bc8a3c */
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bc2abc"></a> `00bc2abc` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bc2ac0"></a> `00bc2ac0` | `fd 7b bc a9` | stp x29,x30,[sp, #-0x40]! | `FALL_THROUGH`
<a id="insn-00bc2ac4"></a> `00bc2ac4` | `f7 0b 00 f9` | str x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bc2ac8"></a> `00bc2ac8` | `f6 57 02 a9` | stp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bc2acc"></a> `00bc2acc` | `f4 4f 03 a9` | stp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bc2ad0"></a> `00bc2ad0` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bc2ad4"></a> `00bc2ad4` | `15 a0 40 a9` | ldp x21,x8,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00bc2ad8"></a> `00bc2ad8` | `bf 02 08 eb` | cmp x21,x8 | `FALL_THROUGH`
<a id="insn-00bc2adc"></a> `00bc2adc` | `61 04 00 54` | b.ne 0x00bc2b68 | `CONDITIONAL_JUMP`
<a id="insn-00bc2ae0"></a> `00bc2ae0` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00bc2ae4"></a> `00bc2ae4` | `f6 03 01 aa` | mov x22,x1 | `FALL_THROUGH`
<a id="insn-00bc2ae8"></a> `00bc2ae8` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-00bc2aec"></a> `00bc2aec` | `14 85 41 f8` | ldr x20,[x8], #0x18 | `FALL_THROUGH`
<a id="insn-00bc2af0"></a> `00bc2af0` | `b3 02 14 cb` | sub x19,x21,x20 | `FALL_THROUGH`
<a id="insn-00bc2af4"></a> `00bc2af4` | `9f 02 08 eb` | cmp x20,x8 | `FALL_THROUGH`
<a id="insn-00bc2af8"></a> `00bc2af8` | `61 fa 7f d3` | lsl x1,x19,#0x1 | `FALL_THROUGH`
<a id="insn-00bc2afc"></a> `00bc2afc` | `00 01 00 54` | b.eq 0x00bc2b1c | `CONDITIONAL_JUMP`
<a id="insn-00bc2b00"></a> `00bc2b00` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bc2b04"></a> `00bc2b04` | `bf 69 00 94` | bl 0x00bdd200 | `UNCONDITIONAL_CALL`
<a id="insn-00bc2b08"></a> `00bc2b08` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00bc2b0c"></a> `00bc2b0c` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00bc2b10"></a> `00bc2b10` | `e8 02 00 f9` | str x8,[x23] | `FALL_THROUGH`
<a id="insn-00bc2b14"></a> `00bc2b14` | `08 02 00 b5` | cbnz x8,0x00bc2b54 | `CONDITIONAL_JUMP`
<a id="insn-00bc2b18"></a> `00bc2b18` | `d6 6d 00 94` | bl 0x00bde270 | `CALL_TERMINATOR`
<a id="insn-00bc2b1c"></a> `00bc2b1c` | `e0 03 01 aa` | mov x0,x1 | `FALL_THROUGH`
<a id="insn-00bc2b20"></a> `00bc2b20` | `98 69 00 94` | bl 0x00bdd180 | `UNCONDITIONAL_CALL`
<a id="insn-00bc2b24"></a> `00bc2b24` | `60 03 00 b4` | cbz x0,0x00bc2b90 | `CONDITIONAL_JUMP`
<a id="insn-00bc2b28"></a> `00bc2b28` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00bc2b2c"></a> `00bc2b2c` | `bf 02 14 eb` | cmp x21,x20 | `FALL_THROUGH`
<a id="insn-00bc2b30"></a> `00bc2b30` | `e0 00 00 54` | b.eq 0x00bc2b4c | `CONDITIONAL_JUMP`
<a id="insn-00bc2b34"></a> `00bc2b34` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00bc2b38"></a> `00bc2b38` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bc2b3c"></a> `00bc2b3c` | `e2 03 13 aa` | mov x2,x19 | `FALL_THROUGH`
<a id="insn-00bc2b40"></a> `00bc2b40` | `f5 03 08 aa` | mov x21,x8 | `FALL_THROUGH`
<a id="insn-00bc2b44"></a> `00bc2b44` | `57 61 00 94` | bl 0x00bdb0a0 | `UNCONDITIONAL_CALL`
<a id="insn-00bc2b48"></a> `00bc2b48` | `e8 03 15 aa` | mov x8,x21 | `FALL_THROUGH`
<a id="insn-00bc2b4c"></a> `00bc2b4c` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00bc2b50"></a> `00bc2b50` | `e8 02 00 f9` | str x8,[x23] | `FALL_THROUGH`
<a id="insn-00bc2b54"></a> `00bc2b54` | `69 fe 42 93` | asr x9,x19,#0x2 | `FALL_THROUGH`
<a id="insn-00bc2b58"></a> `00bc2b58` | `15 01 13 8b` | add x21,x8,x19 | `FALL_THROUGH`
<a id="insn-00bc2b5c"></a> `00bc2b5c` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00bc2b60"></a> `00bc2b60` | `08 0d 09 8b` | add x8,x8,x9, LSL #0x3 | `FALL_THROUGH`
<a id="insn-00bc2b64"></a> `00bc2b64` | `15 a0 00 a9` | stp x21,x8,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00bc2b68"></a> `00bc2b68` | `28 00 40 f9` | ldr x8,[x1] | `FALL_THROUGH`
<a id="insn-00bc2b6c"></a> `00bc2b6c` | `a9 22 00 91` | add x9,x21,#0x8 | `FALL_THROUGH`
<a id="insn-00bc2b70"></a> `00bc2b70` | `09 04 00 f9` | str x9,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00bc2b74"></a> `00bc2b74` | `a8 02 00 f9` | str x8,[x21] | `FALL_THROUGH`
<a id="insn-00bc2b78"></a> `00bc2b78` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bc2b7c"></a> `00bc2b7c` | `f7 0b 40 f9` | ldr x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bc2b80"></a> `00bc2b80` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bc2b84"></a> `00bc2b84` | `fd 7b c4 a8` | ldp x29,x30,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-00bc2b88"></a> `00bc2b88` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bc2b8c"></a> `00bc2b8c` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bc2b90"></a> `00bc2b90` | `b8 6d 00 94` | bl 0x00bde270 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bc2abc`](#insn-00bc2abc) 範囲 `[['00bc2abc', '00bc2adf']]`
  - `CONDITIONAL_JUMP` [`00bc2adc`](#insn-00bc2adc) → [`00bc2b68`](#insn-00bc2b68)
  - `FALL_THROUGH` [`00bc2adc`](#insn-00bc2adc) → [`00bc2ae0`](#insn-00bc2ae0)
- ブロック [`00bc2ae0`](#insn-00bc2ae0) 範囲 `[['00bc2ae0', '00bc2aff']]`
  - `CONDITIONAL_JUMP` [`00bc2afc`](#insn-00bc2afc) → [`00bc2b1c`](#insn-00bc2b1c)
  - `FALL_THROUGH` [`00bc2afc`](#insn-00bc2afc) → [`00bc2b00`](#insn-00bc2b00)
- ブロック [`00bc2b00`](#insn-00bc2b00) 範囲 `[['00bc2b00', '00bc2b17']]`
  - `CONDITIONAL_JUMP` [`00bc2b14`](#insn-00bc2b14) → [`00bc2b54`](#insn-00bc2b54)
  - `FALL_THROUGH` [`00bc2b14`](#insn-00bc2b14) → [`00bc2b18`](#insn-00bc2b18)
- ブロック [`00bc2b18`](#insn-00bc2b18) 範囲 `[['00bc2b18', '00bc2b1b']]`
- ブロック [`00bc2b1c`](#insn-00bc2b1c) 範囲 `[['00bc2b1c', '00bc2b27']]`
  - `CONDITIONAL_JUMP` [`00bc2b24`](#insn-00bc2b24) → [`00bc2b90`](#insn-00bc2b90)
  - `FALL_THROUGH` [`00bc2b24`](#insn-00bc2b24) → [`00bc2b28`](#insn-00bc2b28)
- ブロック [`00bc2b28`](#insn-00bc2b28) 範囲 `[['00bc2b28', '00bc2b33']]`
  - `CONDITIONAL_JUMP` [`00bc2b30`](#insn-00bc2b30) → [`00bc2b4c`](#insn-00bc2b4c)
  - `FALL_THROUGH` [`00bc2b30`](#insn-00bc2b30) → [`00bc2b34`](#insn-00bc2b34)
- ブロック [`00bc2b34`](#insn-00bc2b34) 範囲 `[['00bc2b34', '00bc2b4b']]`
  - `FALL_THROUGH` [`00bc2b48`](#insn-00bc2b48) → [`00bc2b4c`](#insn-00bc2b4c)
- ブロック [`00bc2b4c`](#insn-00bc2b4c) 範囲 `[['00bc2b4c', '00bc2b53']]`
  - `FALL_THROUGH` [`00bc2b50`](#insn-00bc2b50) → [`00bc2b54`](#insn-00bc2b54)
- ブロック [`00bc2b54`](#insn-00bc2b54) 範囲 `[['00bc2b54', '00bc2b67']]`
  - `FALL_THROUGH` [`00bc2b64`](#insn-00bc2b64) → [`00bc2b68`](#insn-00bc2b68)
- ブロック [`00bc2b68`](#insn-00bc2b68) 範囲 `[['00bc2b68', '00bc2b7b']]`
  - `FALL_THROUGH` [`00bc2b78`](#insn-00bc2b78) → [`00bc2b7c`](#insn-00bc2b7c)
- ブロック [`00bc2b7c`](#insn-00bc2b7c) 範囲 `[['00bc2b7c', '00bc2b8f']]`
- ブロック [`00bc2b90`](#insn-00bc2b90) 範囲 `[['00bc2b90', '00bc2b93']]`

## 命令位置別の参照

- [`00bc2ac0`](#insn-00bc2ac0) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc2ac4`](#insn-00bc2ac4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc2ac8`](#insn-00bc2ac8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc2acc`](#insn-00bc2acc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc2adc`](#insn-00bc2adc) → [`00bc2b68`](#insn-00bc2b68) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc2afc`](#insn-00bc2afc) → [`00bc2b1c`](#insn-00bc2b1c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc2b04`](#insn-00bc2b04) → [`00bdd200`](../00bdd/00bdd200.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd200` · 推定シンボル `None` · 推定型 `None`
- [`00bc2b14`](#insn-00bc2b14) → [`00bc2b54`](#insn-00bc2b54) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc2b18`](#insn-00bc2b18) → [`00bde270`](../00bde/00bde270.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde270` · 推定シンボル `None` · 推定型 `None`
- [`00bc2b20`](#insn-00bc2b20) → [`00bdd180`](../00bdd/00bdd180.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd180` · 推定シンボル `None` · 推定型 `None`
- [`00bc2b24`](#insn-00bc2b24) → [`00bc2b90`](#insn-00bc2b90) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc2b30`](#insn-00bc2b30) → [`00bc2b4c`](#insn-00bc2b4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc2b44`](#insn-00bc2b44) → [`00bdb0a0`](../00bdb/00bdb0a0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb0a0` · 推定シンボル `None` · 推定型 `None`
- [`00bc2b78`](#insn-00bc2b78) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc2b7c`](#insn-00bc2b7c) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc2b80`](#insn-00bc2b80) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc2b84`](#insn-00bc2b84) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc2b90`](#insn-00bc2b90) → [`00bde270`](../00bde/00bde270.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde270` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bc2ac0`](#insn-00bc2ac0)

~~~json
{
  "source": "00bc2ac0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc2ac4`](#insn-00bc2ac4)

~~~json
{
  "source": "00bc2ac4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc2ac8`](#insn-00bc2ac8)

~~~json
{
  "source": "00bc2ac8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc2acc`](#insn-00bc2acc)

~~~json
{
  "source": "00bc2acc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc2adc`](#insn-00bc2adc)

~~~json
{
  "source": "00bc2adc",
  "target": "00bc2b68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc2afc`](#insn-00bc2afc)

~~~json
{
  "source": "00bc2afc",
  "target": "00bc2b1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc2b04`](#insn-00bc2b04)

~~~json
{
  "source": "00bc2b04",
  "target": "00bdd200",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc2b14`](#insn-00bc2b14)

~~~json
{
  "source": "00bc2b14",
  "target": "00bc2b54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc2b18`](#insn-00bc2b18)

~~~json
{
  "source": "00bc2b18",
  "target": "00bde270",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc2b20`](#insn-00bc2b20)

~~~json
{
  "source": "00bc2b20",
  "target": "00bdd180",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc2b24`](#insn-00bc2b24)

~~~json
{
  "source": "00bc2b24",
  "target": "00bc2b90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc2b30`](#insn-00bc2b30)

~~~json
{
  "source": "00bc2b30",
  "target": "00bc2b4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc2b44`](#insn-00bc2b44)

~~~json
{
  "source": "00bc2b44",
  "target": "00bdb0a0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc2b78`](#insn-00bc2b78)

~~~json
{
  "source": "00bc2b78",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc2b7c`](#insn-00bc2b7c)

~~~json
{
  "source": "00bc2b7c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc2b80`](#insn-00bc2b80)

~~~json
{
  "source": "00bc2b80",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc2b84`](#insn-00bc2b84)

~~~json
{
  "source": "00bc2b84",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc2b90`](#insn-00bc2b90)

~~~json
{
  "source": "00bc2b90",
  "target": "00bde270",
  "target_space": "ram",
  "resolution": "function"
}
~~~
