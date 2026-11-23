# 00bbfcec

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bbfdb4`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbf/00bbfdb4.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/inspection-0007.md#compare-bced895da71b3b1dc634f2a3b8218d21)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bbfcec",
  "name": "FUN_00bbfcec",
  "size": 216,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e64b40fc99118585de5e0214b939b01a86cd5c43d8462bb96b6abd04611efcd3",
  "source_text_sha256": "e64b40fc99118585de5e0214b939b01a86cd5c43d8462bb96b6abd04611efcd3",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bbfcec",
        "00bbfdc3"
      ]
    ],
    "bytes_sha256": "542dd7b613a27109edebc7bccfdae03fb7e585cace486d6fdb071813af0a0b36",
    "instruction_count": 54,
    "instruction_bytes": 216,
    "body_bytes": 216,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00bbdd50](../00bbd/00bbdd50.md)
- [00bc2e00](../00bc2/00bc2e00.md)

## 呼び出し先

- [00bdaff0](../00bda/00bdaff0.md)
- [00bdd0d0](../00bdd/00bdd0d0.md)
- [00bdd150](../00bdd/00bdd150.md)
- [00bde1c0](../00bde/00bde1c0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1415 bytes

~~~c

void FUN_00bbfcec(undefined8 *param_1,undefined8 *param_2)

{
  void *__dest;
  undefined8 uVar1;
  size_t __n;
  undefined8 *__src;
  undefined8 *puVar2;
  
                    /* try { // try from 00bbfcfc to 00cbfd03 has its CatchHandler @ 00bc8820 */
  puVar2 = (undefined8 *)param_1[1];
                    /* try { // try from 00bbfd08 to 00cbfd17 has its CatchHandler @ 00bc87e0 */
  if (puVar2 == (undefined8 *)param_1[2]) {
    __src = (undefined8 *)*param_1;
    __n = (long)puVar2 - (long)__src;
                    /* try { // try from 00bbfd2c to 00cbfd63 has its CatchHandler @ 00bc8a20 */
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
                    /* try { // try from 00bbfdb4 to 00cbfdc7 has its CatchHandler @ 00bc86d8 */
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bbfcec"></a> `00bbfcec` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bbfcf0"></a> `00bbfcf0` | `fd 7b bc a9` | stp x29,x30,[sp, #-0x40]! | `FALL_THROUGH`
<a id="insn-00bbfcf4"></a> `00bbfcf4` | `f7 0b 00 f9` | str x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbfcf8"></a> `00bbfcf8` | `f6 57 02 a9` | stp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bbfcfc"></a> `00bbfcfc` | `f4 4f 03 a9` | stp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bbfd00"></a> `00bbfd00` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bbfd04"></a> `00bbfd04` | `15 a0 40 a9` | ldp x21,x8,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00bbfd08"></a> `00bbfd08` | `bf 02 08 eb` | cmp x21,x8 | `FALL_THROUGH`
<a id="insn-00bbfd0c"></a> `00bbfd0c` | `61 04 00 54` | b.ne 0x00bbfd98 | `CONDITIONAL_JUMP`
<a id="insn-00bbfd10"></a> `00bbfd10` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00bbfd14"></a> `00bbfd14` | `f6 03 01 aa` | mov x22,x1 | `FALL_THROUGH`
<a id="insn-00bbfd18"></a> `00bbfd18` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-00bbfd1c"></a> `00bbfd1c` | `14 85 41 f8` | ldr x20,[x8], #0x18 | `FALL_THROUGH`
<a id="insn-00bbfd20"></a> `00bbfd20` | `b3 02 14 cb` | sub x19,x21,x20 | `FALL_THROUGH`
<a id="insn-00bbfd24"></a> `00bbfd24` | `9f 02 08 eb` | cmp x20,x8 | `FALL_THROUGH`
<a id="insn-00bbfd28"></a> `00bbfd28` | `61 fa 7f d3` | lsl x1,x19,#0x1 | `FALL_THROUGH`
<a id="insn-00bbfd2c"></a> `00bbfd2c` | `00 01 00 54` | b.eq 0x00bbfd4c | `CONDITIONAL_JUMP`
<a id="insn-00bbfd30"></a> `00bbfd30` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bbfd34"></a> `00bbfd34` | `07 75 00 94` | bl 0x00bdd150 | `UNCONDITIONAL_CALL`
<a id="insn-00bbfd38"></a> `00bbfd38` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00bbfd3c"></a> `00bbfd3c` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00bbfd40"></a> `00bbfd40` | `e8 02 00 f9` | str x8,[x23] | `FALL_THROUGH`
<a id="insn-00bbfd44"></a> `00bbfd44` | `08 02 00 b5` | cbnz x8,0x00bbfd84 | `CONDITIONAL_JUMP`
<a id="insn-00bbfd48"></a> `00bbfd48` | `1e 79 00 94` | bl 0x00bde1c0 | `CALL_TERMINATOR`
<a id="insn-00bbfd4c"></a> `00bbfd4c` | `e0 03 01 aa` | mov x0,x1 | `FALL_THROUGH`
<a id="insn-00bbfd50"></a> `00bbfd50` | `e0 74 00 94` | bl 0x00bdd0d0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbfd54"></a> `00bbfd54` | `60 03 00 b4` | cbz x0,0x00bbfdc0 | `CONDITIONAL_JUMP`
<a id="insn-00bbfd58"></a> `00bbfd58` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00bbfd5c"></a> `00bbfd5c` | `bf 02 14 eb` | cmp x21,x20 | `FALL_THROUGH`
<a id="insn-00bbfd60"></a> `00bbfd60` | `e0 00 00 54` | b.eq 0x00bbfd7c | `CONDITIONAL_JUMP`
<a id="insn-00bbfd64"></a> `00bbfd64` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00bbfd68"></a> `00bbfd68` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bbfd6c"></a> `00bbfd6c` | `e2 03 13 aa` | mov x2,x19 | `FALL_THROUGH`
<a id="insn-00bbfd70"></a> `00bbfd70` | `f5 03 08 aa` | mov x21,x8 | `FALL_THROUGH`
<a id="insn-00bbfd74"></a> `00bbfd74` | `9f 6c 00 94` | bl 0x00bdaff0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbfd78"></a> `00bbfd78` | `e8 03 15 aa` | mov x8,x21 | `FALL_THROUGH`
<a id="insn-00bbfd7c"></a> `00bbfd7c` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00bbfd80"></a> `00bbfd80` | `e8 02 00 f9` | str x8,[x23] | `FALL_THROUGH`
<a id="insn-00bbfd84"></a> `00bbfd84` | `69 fe 42 93` | asr x9,x19,#0x2 | `FALL_THROUGH`
<a id="insn-00bbfd88"></a> `00bbfd88` | `15 01 13 8b` | add x21,x8,x19 | `FALL_THROUGH`
<a id="insn-00bbfd8c"></a> `00bbfd8c` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00bbfd90"></a> `00bbfd90` | `08 0d 09 8b` | add x8,x8,x9, LSL #0x3 | `FALL_THROUGH`
<a id="insn-00bbfd94"></a> `00bbfd94` | `15 a0 00 a9` | stp x21,x8,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00bbfd98"></a> `00bbfd98` | `28 00 40 f9` | ldr x8,[x1] | `FALL_THROUGH`
<a id="insn-00bbfd9c"></a> `00bbfd9c` | `a9 22 00 91` | add x9,x21,#0x8 | `FALL_THROUGH`
<a id="insn-00bbfda0"></a> `00bbfda0` | `09 04 00 f9` | str x9,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00bbfda4"></a> `00bbfda4` | `a8 02 00 f9` | str x8,[x21] | `FALL_THROUGH`
<a id="insn-00bbfda8"></a> `00bbfda8` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bbfdac"></a> `00bbfdac` | `f7 0b 40 f9` | ldr x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbfdb0"></a> `00bbfdb0` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bbfdb4"></a> `00bbfdb4` | `fd 7b c4 a8` | ldp x29,x30,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-00bbfdb8"></a> `00bbfdb8` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bbfdbc"></a> `00bbfdbc` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bbfdc0"></a> `00bbfdc0` | `00 79 00 94` | bl 0x00bde1c0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bbfcec`](#insn-00bbfcec) 範囲 `[['00bbfcec', '00bbfcfb']]`
  - `FALL_THROUGH` [`00bbfcf8`](#insn-00bbfcf8) → [`00bbfcfc`](#insn-00bbfcfc)
- ブロック [`00bbfcfc`](#insn-00bbfcfc) 範囲 `[['00bbfcfc', '00bbfd07']]`
  - `FALL_THROUGH` [`00bbfd04`](#insn-00bbfd04) → [`00bbfd08`](#insn-00bbfd08)
- ブロック [`00bbfd08`](#insn-00bbfd08) 範囲 `[['00bbfd08', '00bbfd0f']]`
  - `CONDITIONAL_JUMP` [`00bbfd0c`](#insn-00bbfd0c) → [`00bbfd98`](#insn-00bbfd98)
  - `FALL_THROUGH` [`00bbfd0c`](#insn-00bbfd0c) → [`00bbfd10`](#insn-00bbfd10)
- ブロック [`00bbfd10`](#insn-00bbfd10) 範囲 `[['00bbfd10', '00bbfd2b']]`
  - `FALL_THROUGH` [`00bbfd28`](#insn-00bbfd28) → [`00bbfd2c`](#insn-00bbfd2c)
- ブロック [`00bbfd2c`](#insn-00bbfd2c) 範囲 `[['00bbfd2c', '00bbfd2f']]`
  - `CONDITIONAL_JUMP` [`00bbfd2c`](#insn-00bbfd2c) → [`00bbfd4c`](#insn-00bbfd4c)
  - `FALL_THROUGH` [`00bbfd2c`](#insn-00bbfd2c) → [`00bbfd30`](#insn-00bbfd30)
- ブロック [`00bbfd30`](#insn-00bbfd30) 範囲 `[['00bbfd30', '00bbfd47']]`
  - `CONDITIONAL_JUMP` [`00bbfd44`](#insn-00bbfd44) → [`00bbfd84`](#insn-00bbfd84)
  - `FALL_THROUGH` [`00bbfd44`](#insn-00bbfd44) → [`00bbfd48`](#insn-00bbfd48)
- ブロック [`00bbfd48`](#insn-00bbfd48) 範囲 `[['00bbfd48', '00bbfd4b']]`
- ブロック [`00bbfd4c`](#insn-00bbfd4c) 範囲 `[['00bbfd4c', '00bbfd57']]`
  - `CONDITIONAL_JUMP` [`00bbfd54`](#insn-00bbfd54) → [`00bbfdc0`](#insn-00bbfdc0)
  - `FALL_THROUGH` [`00bbfd54`](#insn-00bbfd54) → [`00bbfd58`](#insn-00bbfd58)
- ブロック [`00bbfd58`](#insn-00bbfd58) 範囲 `[['00bbfd58', '00bbfd63']]`
  - `CONDITIONAL_JUMP` [`00bbfd60`](#insn-00bbfd60) → [`00bbfd7c`](#insn-00bbfd7c)
  - `FALL_THROUGH` [`00bbfd60`](#insn-00bbfd60) → [`00bbfd64`](#insn-00bbfd64)
- ブロック [`00bbfd64`](#insn-00bbfd64) 範囲 `[['00bbfd64', '00bbfd7b']]`
  - `FALL_THROUGH` [`00bbfd78`](#insn-00bbfd78) → [`00bbfd7c`](#insn-00bbfd7c)
- ブロック [`00bbfd7c`](#insn-00bbfd7c) 範囲 `[['00bbfd7c', '00bbfd83']]`
  - `FALL_THROUGH` [`00bbfd80`](#insn-00bbfd80) → [`00bbfd84`](#insn-00bbfd84)
- ブロック [`00bbfd84`](#insn-00bbfd84) 範囲 `[['00bbfd84', '00bbfd97']]`
  - `FALL_THROUGH` [`00bbfd94`](#insn-00bbfd94) → [`00bbfd98`](#insn-00bbfd98)
- ブロック [`00bbfd98`](#insn-00bbfd98) 範囲 `[['00bbfd98', '00bbfdb3']]`
  - `FALL_THROUGH` [`00bbfdb0`](#insn-00bbfdb0) → [`00bbfdb4`](#insn-00bbfdb4)
- ブロック [`00bbfdb4`](#insn-00bbfdb4) 範囲 `[['00bbfdb4', '00bbfdbf']]`
- ブロック [`00bbfdc0`](#insn-00bbfdc0) 範囲 `[['00bbfdc0', '00bbfdc3']]`

## 命令位置別の参照

- [`00bbfcf0`](#insn-00bbfcf0) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfcf4`](#insn-00bbfcf4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfcf8`](#insn-00bbfcf8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfcfc`](#insn-00bbfcfc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfd0c`](#insn-00bbfd0c) → [`00bbfd98`](#insn-00bbfd98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfd2c`](#insn-00bbfd2c) → [`00bbfd4c`](#insn-00bbfd4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfd34`](#insn-00bbfd34) → [`00bdd150`](../00bdd/00bdd150.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd150` · 推定シンボル `None` · 推定型 `None`
- [`00bbfd44`](#insn-00bbfd44) → [`00bbfd84`](#insn-00bbfd84) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfd48`](#insn-00bbfd48) → [`00bde1c0`](../00bde/00bde1c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde1c0` · 推定シンボル `None` · 推定型 `None`
- [`00bbfd50`](#insn-00bbfd50) → [`00bdd0d0`](../00bdd/00bdd0d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd0d0` · 推定シンボル `None` · 推定型 `None`
- [`00bbfd54`](#insn-00bbfd54) → [`00bbfdc0`](#insn-00bbfdc0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfd60`](#insn-00bbfd60) → [`00bbfd7c`](#insn-00bbfd7c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfd74`](#insn-00bbfd74) → [`00bdaff0`](../00bda/00bdaff0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaff0` · 推定シンボル `None` · 推定型 `None`
- [`00bbfda8`](#insn-00bbfda8) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfdac`](#insn-00bbfdac) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfdb0`](#insn-00bbfdb0) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfdb4`](#insn-00bbfdb4) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfdc0`](#insn-00bbfdc0) → [`00bde1c0`](../00bde/00bde1c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde1c0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bbfcf0`](#insn-00bbfcf0)

~~~json
{
  "source": "00bbfcf0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfcf4`](#insn-00bbfcf4)

~~~json
{
  "source": "00bbfcf4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfcf8`](#insn-00bbfcf8)

~~~json
{
  "source": "00bbfcf8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfcfc`](#insn-00bbfcfc)

~~~json
{
  "source": "00bbfcfc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfd0c`](#insn-00bbfd0c)

~~~json
{
  "source": "00bbfd0c",
  "target": "00bbfd98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfd2c`](#insn-00bbfd2c)

~~~json
{
  "source": "00bbfd2c",
  "target": "00bbfd4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfd34`](#insn-00bbfd34)

~~~json
{
  "source": "00bbfd34",
  "target": "00bdd150",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbfd44`](#insn-00bbfd44)

~~~json
{
  "source": "00bbfd44",
  "target": "00bbfd84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfd48`](#insn-00bbfd48)

~~~json
{
  "source": "00bbfd48",
  "target": "00bde1c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbfd50`](#insn-00bbfd50)

~~~json
{
  "source": "00bbfd50",
  "target": "00bdd0d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbfd54`](#insn-00bbfd54)

~~~json
{
  "source": "00bbfd54",
  "target": "00bbfdc0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfd60`](#insn-00bbfd60)

~~~json
{
  "source": "00bbfd60",
  "target": "00bbfd7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfd74`](#insn-00bbfd74)

~~~json
{
  "source": "00bbfd74",
  "target": "00bdaff0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbfda8`](#insn-00bbfda8)

~~~json
{
  "source": "00bbfda8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfdac`](#insn-00bbfdac)

~~~json
{
  "source": "00bbfdac",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfdb0`](#insn-00bbfdb0)

~~~json
{
  "source": "00bbfdb0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfdb4`](#insn-00bbfdb4)

~~~json
{
  "source": "00bbfdb4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfdc0`](#insn-00bbfdc0)

~~~json
{
  "source": "00bbfdc0",
  "target": "00bde1c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
