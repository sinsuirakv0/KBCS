# 00bbdcd8

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bbdc10`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbd/00bbdc10.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/no_difference_in_scope-0026.md#compare-ea56c8d2febec5553d688d9d95fc43c7)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bbdd1c`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbdd1c.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/no_difference_in_scope-0019.md#compare-c79f347f6949c0dc80576a302e5d35c7)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bbdcd8",
  "name": "FUN_00bbdcd8",
  "size": 140,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "eff7d43d021d0ad2a702d57539234b2e499b2b859ff011d2bee5709c6102af2c",
  "source_text_sha256": "eff7d43d021d0ad2a702d57539234b2e499b2b859ff011d2bee5709c6102af2c",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bbdcd8",
        "00bbdd63"
      ]
    ],
    "bytes_sha256": "72ba3b5ad2a48e8bfc3adc65e87cd8bb30a7c475e3309ff484d344a3a826d848",
    "instruction_count": 35,
    "instruction_bytes": 140,
    "body_bytes": 140,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00bbd2c4](../00bbd/00bbd2c4.md)
- [00bbde18](../00bbd/00bbde18.md)
- [00bbf358](../00bbf/00bbf358.md)
- [00bc9384](../00bc9/00bc9384.md)

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1107 bytes

~~~c

undefined1  [16] FUN_00bbdcd8(long *param_1,ulong param_2)

{
  byte *pbVar1;
  byte *pbVar2;
  byte *pbVar3;
  undefined1 auVar4 [16];
  
  auVar4._0_8_ = (byte *)*param_1;
  pbVar1 = (byte *)param_1[1];
  pbVar2 = auVar4._0_8_;
                    /* try { // try from 00bbdcf4 to 00cbdcff has its CatchHandler @ 00bbe14c */
                    /* try { // try from 00bbdd00 to 00cbdd0f has its CatchHandler @ 00bbe148 */
  if ((((param_2 & 1) != 0) && (auVar4._0_8_ != pbVar1)) && (*auVar4._0_8_ == 0x6e)) {
    pbVar2 = auVar4._0_8_ + 1;
    *param_1 = (long)pbVar2;
  }
  if ((pbVar1 == pbVar2) || (*pbVar2 - 0x3a < 0xfffffff6)) {
                    /* try { // try from 00bbdd34 to 00cbdd3f has its CatchHandler @ 00bbe14c */
    return ZEXT816(0);
  }
  do {
                    /* try { // try from 00bbdd40 to 00cbdd4f has its CatchHandler @ 00bbe148 */
    pbVar3 = pbVar2;
    if (*pbVar2 - 0x3a < 0xfffffff6) break;
    pbVar2 = pbVar2 + 1;
    *param_1 = (long)pbVar2;
    pbVar3 = pbVar1;
  } while (pbVar2 != pbVar1);
  auVar4._8_8_ = (long)pbVar3 - (long)auVar4._0_8_;
  return auVar4;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bbdcd8"></a> `00bbdcd8` | `5f 24 03 d5` | bti c | `FALL_THROUGH`
<a id="insn-00bbdcdc"></a> `00bbdcdc` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00bbdce0"></a> `00bbdce0` | `00 00 40 f9` | ldr x0,[x0] | `FALL_THROUGH`
<a id="insn-00bbdce4"></a> `00bbdce4` | `09 05 40 f9` | ldr x9,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00bbdce8"></a> `00bbdce8` | `ea 03 00 aa` | mov x10,x0 | `FALL_THROUGH`
<a id="insn-00bbdcec"></a> `00bbdcec` | `41 01 00 36` | tbz w1,#0x0,0x00bbdd14 | `CONDITIONAL_JUMP`
<a id="insn-00bbdcf0"></a> `00bbdcf0` | `1f 00 09 eb` | cmp x0,x9 | `FALL_THROUGH`
<a id="insn-00bbdcf4"></a> `00bbdcf4` | `ea 03 00 aa` | mov x10,x0 | `FALL_THROUGH`
<a id="insn-00bbdcf8"></a> `00bbdcf8` | `e0 00 00 54` | b.eq 0x00bbdd14 | `CONDITIONAL_JUMP`
<a id="insn-00bbdcfc"></a> `00bbdcfc` | `0a 00 40 39` | ldrb w10,[x0] | `FALL_THROUGH`
<a id="insn-00bbdd00"></a> `00bbdd00` | `5f b9 01 71` | cmp w10,#0x6e | `FALL_THROUGH`
<a id="insn-00bbdd04"></a> `00bbdd04` | `ea 03 00 aa` | mov x10,x0 | `FALL_THROUGH`
<a id="insn-00bbdd08"></a> `00bbdd08` | `61 00 00 54` | b.ne 0x00bbdd14 | `CONDITIONAL_JUMP`
<a id="insn-00bbdd0c"></a> `00bbdd0c` | `0a 04 00 91` | add x10,x0,#0x1 | `FALL_THROUGH`
<a id="insn-00bbdd10"></a> `00bbdd10` | `0a 01 00 f9` | str x10,[x8] | `FALL_THROUGH`
<a id="insn-00bbdd14"></a> `00bbdd14` | `3f 01 0a eb` | cmp x9,x10 | `FALL_THROUGH`
<a id="insn-00bbdd18"></a> `00bbdd18` | `a0 00 00 54` | b.eq 0x00bbdd2c | `CONDITIONAL_JUMP`
<a id="insn-00bbdd1c"></a> `00bbdd1c` | `4b 01 40 39` | ldrb w11,[x10] | `FALL_THROUGH`
<a id="insn-00bbdd20"></a> `00bbdd20` | `6b e9 00 51` | sub w11,w11,#0x3a | `FALL_THROUGH`
<a id="insn-00bbdd24"></a> `00bbdd24` | `7f 29 00 31` | cmn w11,#0xa | `FALL_THROUGH`
<a id="insn-00bbdd28"></a> `00bbdd28` | `82 00 00 54` | b.cs 0x00bbdd38 | `CONDITIONAL_JUMP`
<a id="insn-00bbdd2c"></a> `00bbdd2c` | `e0 03 1f aa` | mov x0,xzr | `FALL_THROUGH`
<a id="insn-00bbdd30"></a> `00bbdd30` | `e1 03 1f aa` | mov x1,xzr | `FALL_THROUGH`
<a id="insn-00bbdd34"></a> `00bbdd34` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bbdd38"></a> `00bbdd38` | `4b 01 40 39` | ldrb w11,[x10] | `FALL_THROUGH`
<a id="insn-00bbdd3c"></a> `00bbdd3c` | `6b e9 00 51` | sub w11,w11,#0x3a | `FALL_THROUGH`
<a id="insn-00bbdd40"></a> `00bbdd40` | `7f 29 00 31` | cmn w11,#0xa | `FALL_THROUGH`
<a id="insn-00bbdd44"></a> `00bbdd44` | `c3 00 00 54` | b.cc 0x00bbdd5c | `CONDITIONAL_JUMP`
<a id="insn-00bbdd48"></a> `00bbdd48` | `4a 05 00 91` | add x10,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00bbdd4c"></a> `00bbdd4c` | `5f 01 09 eb` | cmp x10,x9 | `FALL_THROUGH`
<a id="insn-00bbdd50"></a> `00bbdd50` | `0a 01 00 f9` | str x10,[x8] | `FALL_THROUGH`
<a id="insn-00bbdd54"></a> `00bbdd54` | `21 ff ff 54` | b.ne 0x00bbdd38 | `CONDITIONAL_JUMP`
<a id="insn-00bbdd58"></a> `00bbdd58` | `ea 03 09 aa` | mov x10,x9 | `FALL_THROUGH`
<a id="insn-00bbdd5c"></a> `00bbdd5c` | `41 01 00 cb` | sub x1,x10,x0 | `FALL_THROUGH`
<a id="insn-00bbdd60"></a> `00bbdd60` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bbdcd8`](#insn-00bbdcd8) 範囲 `[['00bbdcd8', '00bbdcef']]`
  - `CONDITIONAL_JUMP` [`00bbdcec`](#insn-00bbdcec) → [`00bbdd14`](#insn-00bbdd14)
  - `FALL_THROUGH` [`00bbdcec`](#insn-00bbdcec) → [`00bbdcf0`](#insn-00bbdcf0)
- ブロック [`00bbdcf0`](#insn-00bbdcf0) 範囲 `[['00bbdcf0', '00bbdcf3']]`
  - `FALL_THROUGH` [`00bbdcf0`](#insn-00bbdcf0) → [`00bbdcf4`](#insn-00bbdcf4)
- ブロック [`00bbdcf4`](#insn-00bbdcf4) 範囲 `[['00bbdcf4', '00bbdcfb']]`
  - `CONDITIONAL_JUMP` [`00bbdcf8`](#insn-00bbdcf8) → [`00bbdd14`](#insn-00bbdd14)
  - `FALL_THROUGH` [`00bbdcf8`](#insn-00bbdcf8) → [`00bbdcfc`](#insn-00bbdcfc)
- ブロック [`00bbdcfc`](#insn-00bbdcfc) 範囲 `[['00bbdcfc', '00bbdcff']]`
  - `FALL_THROUGH` [`00bbdcfc`](#insn-00bbdcfc) → [`00bbdd00`](#insn-00bbdd00)
- ブロック [`00bbdd00`](#insn-00bbdd00) 範囲 `[['00bbdd00', '00bbdd0b']]`
  - `CONDITIONAL_JUMP` [`00bbdd08`](#insn-00bbdd08) → [`00bbdd14`](#insn-00bbdd14)
  - `FALL_THROUGH` [`00bbdd08`](#insn-00bbdd08) → [`00bbdd0c`](#insn-00bbdd0c)
- ブロック [`00bbdd0c`](#insn-00bbdd0c) 範囲 `[['00bbdd0c', '00bbdd13']]`
  - `FALL_THROUGH` [`00bbdd10`](#insn-00bbdd10) → [`00bbdd14`](#insn-00bbdd14)
- ブロック [`00bbdd14`](#insn-00bbdd14) 範囲 `[['00bbdd14', '00bbdd1b']]`
  - `CONDITIONAL_JUMP` [`00bbdd18`](#insn-00bbdd18) → [`00bbdd2c`](#insn-00bbdd2c)
  - `FALL_THROUGH` [`00bbdd18`](#insn-00bbdd18) → [`00bbdd1c`](#insn-00bbdd1c)
- ブロック [`00bbdd1c`](#insn-00bbdd1c) 範囲 `[['00bbdd1c', '00bbdd2b']]`
  - `CONDITIONAL_JUMP` [`00bbdd28`](#insn-00bbdd28) → [`00bbdd38`](#insn-00bbdd38)
  - `FALL_THROUGH` [`00bbdd28`](#insn-00bbdd28) → [`00bbdd2c`](#insn-00bbdd2c)
- ブロック [`00bbdd2c`](#insn-00bbdd2c) 範囲 `[['00bbdd2c', '00bbdd33']]`
  - `FALL_THROUGH` [`00bbdd30`](#insn-00bbdd30) → [`00bbdd34`](#insn-00bbdd34)
- ブロック [`00bbdd34`](#insn-00bbdd34) 範囲 `[['00bbdd34', '00bbdd37']]`
- ブロック [`00bbdd38`](#insn-00bbdd38) 範囲 `[['00bbdd38', '00bbdd3f']]`
  - `FALL_THROUGH` [`00bbdd3c`](#insn-00bbdd3c) → [`00bbdd40`](#insn-00bbdd40)
- ブロック [`00bbdd40`](#insn-00bbdd40) 範囲 `[['00bbdd40', '00bbdd47']]`
  - `CONDITIONAL_JUMP` [`00bbdd44`](#insn-00bbdd44) → [`00bbdd5c`](#insn-00bbdd5c)
  - `FALL_THROUGH` [`00bbdd44`](#insn-00bbdd44) → [`00bbdd48`](#insn-00bbdd48)
- ブロック [`00bbdd48`](#insn-00bbdd48) 範囲 `[['00bbdd48', '00bbdd57']]`
  - `CONDITIONAL_JUMP` [`00bbdd54`](#insn-00bbdd54) → [`00bbdd38`](#insn-00bbdd38)
  - `FALL_THROUGH` [`00bbdd54`](#insn-00bbdd54) → [`00bbdd58`](#insn-00bbdd58)
- ブロック [`00bbdd58`](#insn-00bbdd58) 範囲 `[['00bbdd58', '00bbdd5b']]`
  - `FALL_THROUGH` [`00bbdd58`](#insn-00bbdd58) → [`00bbdd5c`](#insn-00bbdd5c)
- ブロック [`00bbdd5c`](#insn-00bbdd5c) 範囲 `[['00bbdd5c', '00bbdd63']]`

## 命令位置別の参照

- [`00bbdcec`](#insn-00bbdcec) → [`00bbdd14`](#insn-00bbdd14) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdcf8`](#insn-00bbdcf8) → [`00bbdd14`](#insn-00bbdd14) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdd08`](#insn-00bbdd08) → [`00bbdd14`](#insn-00bbdd14) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdd18`](#insn-00bbdd18) → [`00bbdd2c`](#insn-00bbdd2c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdd28`](#insn-00bbdd28) → [`00bbdd38`](#insn-00bbdd38) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdd44`](#insn-00bbdd44) → [`00bbdd5c`](#insn-00bbdd5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdd54`](#insn-00bbdd54) → [`00bbdd38`](#insn-00bbdd38) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bbdcec`](#insn-00bbdcec)

~~~json
{
  "source": "00bbdcec",
  "target": "00bbdd14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdcf8`](#insn-00bbdcf8)

~~~json
{
  "source": "00bbdcf8",
  "target": "00bbdd14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdd08`](#insn-00bbdd08)

~~~json
{
  "source": "00bbdd08",
  "target": "00bbdd14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdd18`](#insn-00bbdd18)

~~~json
{
  "source": "00bbdd18",
  "target": "00bbdd2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdd28`](#insn-00bbdd28)

~~~json
{
  "source": "00bbdd28",
  "target": "00bbdd38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdd44`](#insn-00bbdd44)

~~~json
{
  "source": "00bbdd44",
  "target": "00bbdd5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdd54`](#insn-00bbdd54)

~~~json
{
  "source": "00bbdd54",
  "target": "00bbdd38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
