# 00bbdd1c

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bbdcd8`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbdcd8.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/no_difference_in_scope-0019.md#compare-c79f347f6949c0dc80576a302e5d35c7)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c3a764`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3a/00c3a764.md) · 移動量 `+0x7ca48`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0077.md#compare-772e5a44e64a09592ed8734dce22d16f)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bbdd1c",
  "name": "FUN_00bbdd1c",
  "size": 140,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "05327dc88c6fb177b473859e41e7b3b9d46a8040d10169ab86318f8f3e8c6b80",
  "source_text_sha256": "05327dc88c6fb177b473859e41e7b3b9d46a8040d10169ab86318f8f3e8c6b80",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bbdd1c",
        "00bbdda7"
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

- [00bbd308](../00bbd/00bbd308.md)
- [00bbde5c](../00bbd/00bbde5c.md)
- [00bbf39c](../00bbf/00bbf39c.md)
- [00bc93c8](../00bc9/00bc93c8.md)

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1107 bytes

~~~c

undefined1  [16] FUN_00bbdd1c(long *param_1,ulong param_2)

{
  byte *pbVar1;
  byte *pbVar2;
  byte *pbVar3;
  undefined1 auVar4 [16];
  
  auVar4._0_8_ = (byte *)*param_1;
  pbVar1 = (byte *)param_1[1];
  pbVar2 = auVar4._0_8_;
                    /* try { // try from 00bbdd38 to 00cbdd43 has its CatchHandler @ 00bbe190 */
                    /* try { // try from 00bbdd44 to 00cbdd53 has its CatchHandler @ 00bbe18c */
  if ((((param_2 & 1) != 0) && (auVar4._0_8_ != pbVar1)) && (*auVar4._0_8_ == 0x6e)) {
    pbVar2 = auVar4._0_8_ + 1;
    *param_1 = (long)pbVar2;
  }
  if ((pbVar1 == pbVar2) || (*pbVar2 - 0x3a < 0xfffffff6)) {
                    /* try { // try from 00bbdd78 to 00cbdd83 has its CatchHandler @ 00bbe190 */
    return ZEXT816(0);
  }
  do {
                    /* try { // try from 00bbdd84 to 00cbdd93 has its CatchHandler @ 00bbe18c */
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
<a id="insn-00bbdd1c"></a> `00bbdd1c` | `5f 24 03 d5` | bti c | `FALL_THROUGH`
<a id="insn-00bbdd20"></a> `00bbdd20` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00bbdd24"></a> `00bbdd24` | `00 00 40 f9` | ldr x0,[x0] | `FALL_THROUGH`
<a id="insn-00bbdd28"></a> `00bbdd28` | `09 05 40 f9` | ldr x9,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00bbdd2c"></a> `00bbdd2c` | `ea 03 00 aa` | mov x10,x0 | `FALL_THROUGH`
<a id="insn-00bbdd30"></a> `00bbdd30` | `41 01 00 36` | tbz w1,#0x0,0x00bbdd58 | `CONDITIONAL_JUMP`
<a id="insn-00bbdd34"></a> `00bbdd34` | `1f 00 09 eb` | cmp x0,x9 | `FALL_THROUGH`
<a id="insn-00bbdd38"></a> `00bbdd38` | `ea 03 00 aa` | mov x10,x0 | `FALL_THROUGH`
<a id="insn-00bbdd3c"></a> `00bbdd3c` | `e0 00 00 54` | b.eq 0x00bbdd58 | `CONDITIONAL_JUMP`
<a id="insn-00bbdd40"></a> `00bbdd40` | `0a 00 40 39` | ldrb w10,[x0] | `FALL_THROUGH`
<a id="insn-00bbdd44"></a> `00bbdd44` | `5f b9 01 71` | cmp w10,#0x6e | `FALL_THROUGH`
<a id="insn-00bbdd48"></a> `00bbdd48` | `ea 03 00 aa` | mov x10,x0 | `FALL_THROUGH`
<a id="insn-00bbdd4c"></a> `00bbdd4c` | `61 00 00 54` | b.ne 0x00bbdd58 | `CONDITIONAL_JUMP`
<a id="insn-00bbdd50"></a> `00bbdd50` | `0a 04 00 91` | add x10,x0,#0x1 | `FALL_THROUGH`
<a id="insn-00bbdd54"></a> `00bbdd54` | `0a 01 00 f9` | str x10,[x8] | `FALL_THROUGH`
<a id="insn-00bbdd58"></a> `00bbdd58` | `3f 01 0a eb` | cmp x9,x10 | `FALL_THROUGH`
<a id="insn-00bbdd5c"></a> `00bbdd5c` | `a0 00 00 54` | b.eq 0x00bbdd70 | `CONDITIONAL_JUMP`
<a id="insn-00bbdd60"></a> `00bbdd60` | `4b 01 40 39` | ldrb w11,[x10] | `FALL_THROUGH`
<a id="insn-00bbdd64"></a> `00bbdd64` | `6b e9 00 51` | sub w11,w11,#0x3a | `FALL_THROUGH`
<a id="insn-00bbdd68"></a> `00bbdd68` | `7f 29 00 31` | cmn w11,#0xa | `FALL_THROUGH`
<a id="insn-00bbdd6c"></a> `00bbdd6c` | `82 00 00 54` | b.cs 0x00bbdd7c | `CONDITIONAL_JUMP`
<a id="insn-00bbdd70"></a> `00bbdd70` | `e0 03 1f aa` | mov x0,xzr | `FALL_THROUGH`
<a id="insn-00bbdd74"></a> `00bbdd74` | `e1 03 1f aa` | mov x1,xzr | `FALL_THROUGH`
<a id="insn-00bbdd78"></a> `00bbdd78` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bbdd7c"></a> `00bbdd7c` | `4b 01 40 39` | ldrb w11,[x10] | `FALL_THROUGH`
<a id="insn-00bbdd80"></a> `00bbdd80` | `6b e9 00 51` | sub w11,w11,#0x3a | `FALL_THROUGH`
<a id="insn-00bbdd84"></a> `00bbdd84` | `7f 29 00 31` | cmn w11,#0xa | `FALL_THROUGH`
<a id="insn-00bbdd88"></a> `00bbdd88` | `c3 00 00 54` | b.cc 0x00bbdda0 | `CONDITIONAL_JUMP`
<a id="insn-00bbdd8c"></a> `00bbdd8c` | `4a 05 00 91` | add x10,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00bbdd90"></a> `00bbdd90` | `5f 01 09 eb` | cmp x10,x9 | `FALL_THROUGH`
<a id="insn-00bbdd94"></a> `00bbdd94` | `0a 01 00 f9` | str x10,[x8] | `FALL_THROUGH`
<a id="insn-00bbdd98"></a> `00bbdd98` | `21 ff ff 54` | b.ne 0x00bbdd7c | `CONDITIONAL_JUMP`
<a id="insn-00bbdd9c"></a> `00bbdd9c` | `ea 03 09 aa` | mov x10,x9 | `FALL_THROUGH`
<a id="insn-00bbdda0"></a> `00bbdda0` | `41 01 00 cb` | sub x1,x10,x0 | `FALL_THROUGH`
<a id="insn-00bbdda4"></a> `00bbdda4` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bbdd1c`](#insn-00bbdd1c) 範囲 `[['00bbdd1c', '00bbdd33']]`
  - `CONDITIONAL_JUMP` [`00bbdd30`](#insn-00bbdd30) → [`00bbdd58`](#insn-00bbdd58)
  - `FALL_THROUGH` [`00bbdd30`](#insn-00bbdd30) → [`00bbdd34`](#insn-00bbdd34)
- ブロック [`00bbdd34`](#insn-00bbdd34) 範囲 `[['00bbdd34', '00bbdd37']]`
  - `FALL_THROUGH` [`00bbdd34`](#insn-00bbdd34) → [`00bbdd38`](#insn-00bbdd38)
- ブロック [`00bbdd38`](#insn-00bbdd38) 範囲 `[['00bbdd38', '00bbdd3f']]`
  - `CONDITIONAL_JUMP` [`00bbdd3c`](#insn-00bbdd3c) → [`00bbdd58`](#insn-00bbdd58)
  - `FALL_THROUGH` [`00bbdd3c`](#insn-00bbdd3c) → [`00bbdd40`](#insn-00bbdd40)
- ブロック [`00bbdd40`](#insn-00bbdd40) 範囲 `[['00bbdd40', '00bbdd43']]`
  - `FALL_THROUGH` [`00bbdd40`](#insn-00bbdd40) → [`00bbdd44`](#insn-00bbdd44)
- ブロック [`00bbdd44`](#insn-00bbdd44) 範囲 `[['00bbdd44', '00bbdd4f']]`
  - `CONDITIONAL_JUMP` [`00bbdd4c`](#insn-00bbdd4c) → [`00bbdd58`](#insn-00bbdd58)
  - `FALL_THROUGH` [`00bbdd4c`](#insn-00bbdd4c) → [`00bbdd50`](#insn-00bbdd50)
- ブロック [`00bbdd50`](#insn-00bbdd50) 範囲 `[['00bbdd50', '00bbdd57']]`
  - `FALL_THROUGH` [`00bbdd54`](#insn-00bbdd54) → [`00bbdd58`](#insn-00bbdd58)
- ブロック [`00bbdd58`](#insn-00bbdd58) 範囲 `[['00bbdd58', '00bbdd5f']]`
  - `CONDITIONAL_JUMP` [`00bbdd5c`](#insn-00bbdd5c) → [`00bbdd70`](#insn-00bbdd70)
  - `FALL_THROUGH` [`00bbdd5c`](#insn-00bbdd5c) → [`00bbdd60`](#insn-00bbdd60)
- ブロック [`00bbdd60`](#insn-00bbdd60) 範囲 `[['00bbdd60', '00bbdd6f']]`
  - `CONDITIONAL_JUMP` [`00bbdd6c`](#insn-00bbdd6c) → [`00bbdd7c`](#insn-00bbdd7c)
  - `FALL_THROUGH` [`00bbdd6c`](#insn-00bbdd6c) → [`00bbdd70`](#insn-00bbdd70)
- ブロック [`00bbdd70`](#insn-00bbdd70) 範囲 `[['00bbdd70', '00bbdd77']]`
  - `FALL_THROUGH` [`00bbdd74`](#insn-00bbdd74) → [`00bbdd78`](#insn-00bbdd78)
- ブロック [`00bbdd78`](#insn-00bbdd78) 範囲 `[['00bbdd78', '00bbdd7b']]`
- ブロック [`00bbdd7c`](#insn-00bbdd7c) 範囲 `[['00bbdd7c', '00bbdd83']]`
  - `FALL_THROUGH` [`00bbdd80`](#insn-00bbdd80) → [`00bbdd84`](#insn-00bbdd84)
- ブロック [`00bbdd84`](#insn-00bbdd84) 範囲 `[['00bbdd84', '00bbdd8b']]`
  - `CONDITIONAL_JUMP` [`00bbdd88`](#insn-00bbdd88) → [`00bbdda0`](#insn-00bbdda0)
  - `FALL_THROUGH` [`00bbdd88`](#insn-00bbdd88) → [`00bbdd8c`](#insn-00bbdd8c)
- ブロック [`00bbdd8c`](#insn-00bbdd8c) 範囲 `[['00bbdd8c', '00bbdd9b']]`
  - `CONDITIONAL_JUMP` [`00bbdd98`](#insn-00bbdd98) → [`00bbdd7c`](#insn-00bbdd7c)
  - `FALL_THROUGH` [`00bbdd98`](#insn-00bbdd98) → [`00bbdd9c`](#insn-00bbdd9c)
- ブロック [`00bbdd9c`](#insn-00bbdd9c) 範囲 `[['00bbdd9c', '00bbdd9f']]`
  - `FALL_THROUGH` [`00bbdd9c`](#insn-00bbdd9c) → [`00bbdda0`](#insn-00bbdda0)
- ブロック [`00bbdda0`](#insn-00bbdda0) 範囲 `[['00bbdda0', '00bbdda7']]`

## 命令位置別の参照

- [`00bbdd30`](#insn-00bbdd30) → [`00bbdd58`](#insn-00bbdd58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdd3c`](#insn-00bbdd3c) → [`00bbdd58`](#insn-00bbdd58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdd4c`](#insn-00bbdd4c) → [`00bbdd58`](#insn-00bbdd58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdd5c`](#insn-00bbdd5c) → [`00bbdd70`](#insn-00bbdd70) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdd6c`](#insn-00bbdd6c) → [`00bbdd7c`](#insn-00bbdd7c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdd88`](#insn-00bbdd88) → [`00bbdda0`](#insn-00bbdda0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdd98`](#insn-00bbdd98) → [`00bbdd7c`](#insn-00bbdd7c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bbdd30`](#insn-00bbdd30)

~~~json
{
  "source": "00bbdd30",
  "target": "00bbdd58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdd3c`](#insn-00bbdd3c)

~~~json
{
  "source": "00bbdd3c",
  "target": "00bbdd58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdd4c`](#insn-00bbdd4c)

~~~json
{
  "source": "00bbdd4c",
  "target": "00bbdd58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdd5c`](#insn-00bbdd5c)

~~~json
{
  "source": "00bbdd5c",
  "target": "00bbdd70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdd6c`](#insn-00bbdd6c)

~~~json
{
  "source": "00bbdd6c",
  "target": "00bbdd7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdd88`](#insn-00bbdd88)

~~~json
{
  "source": "00bbdd88",
  "target": "00bbdda0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdd98`](#insn-00bbdd98)

~~~json
{
  "source": "00bbdd98",
  "target": "00bbdd7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
