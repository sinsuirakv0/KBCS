# 00bccab0

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bcc688`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc688.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/alignment_unresolved-0010.md#compare-f898c60c92fca50b7187c14582ee65b3)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bccb4c`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcc/00bccb4c.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/alignment_unresolved-0011.md#compare-a775bfa83135a0e75e33fba3769e691c)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bccab0",
  "name": "_ZN8firebase4auth11jnilistener15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm",
  "size": 108,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "aa4fe6ee52d09f6b77e21829b53d3ebe57246e852263bcd5067a03f062af32cb",
  "source_text_sha256": "aa4fe6ee52d09f6b77e21829b53d3ebe57246e852263bcd5067a03f062af32cb",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bccab0",
        "00bccb1b"
      ]
    ],
    "bytes_sha256": "c9ddf65bb8bcd3f03a85a511fd5d4fec90596030fe08c80eba4ff47c84c174bb",
    "instruction_count": 27,
    "instruction_bytes": 108,
    "body_bytes": 108,
    "indirect": 1,
    "unresolved": 1
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5af60](../00c5a/00c5af60.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 681 bytes

~~~c

bool _ZN8firebase4auth11jnilistener15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm
               (long *param_1,undefined8 param_2,undefined8 param_3)

{
  bool bVar1;
  int iVar2;
  
  if (DAT_011267f8 == '\0') {
                    /* try { // try from 00bccaf0 to 00cccb07 has its CatchHandler @ 00bce908 */
    iVar2 = (**(code **)(*param_1 + 0x6b8))(param_1,DAT_011267f0,param_2,param_3);
    _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(param_1);
    DAT_011267f8 = iVar2 == 0;
                    /* try { // try from 00bccb08 to 00cccbbb has its CatchHandler @ 00bcc5d0 */
    bVar1 = (bool)DAT_011267f8;
  }
  else {
    bVar1 = false;
  }
  return bVar1;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bccab0"></a> `00bccab0` | `f5 0f 1d f8` | str x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00bccab4"></a> `00bccab4` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bccab8"></a> `00bccab8` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bccabc"></a> `00bccabc` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bccac0"></a> `00bccac0` | `d5 2a 00 d0` | adrp x21,0x1126000 | `FALL_THROUGH`
<a id="insn-00bccac4"></a> `00bccac4` | `a8 e2 5f 39` | ldrb w8,[x21, #0x7f8] | `FALL_THROUGH`
<a id="insn-00bccac8"></a> `00bccac8` | `68 00 00 34` | cbz w8,0x00bccad4 | `CONDITIONAL_JUMP`
<a id="insn-00bccacc"></a> `00bccacc` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00bccad0"></a> `00bccad0` | `0f 00 00 14` | b 0x00bccb0c | `UNCONDITIONAL_JUMP`
<a id="insn-00bccad4"></a> `00bccad4` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bccad8"></a> `00bccad8` | `c9 2a 00 d0` | adrp x9,0x1126000 | `FALL_THROUGH`
<a id="insn-00bccadc"></a> `00bccadc` | `e3 03 02 aa` | mov x3,x2 | `FALL_THROUGH`
<a id="insn-00bccae0"></a> `00bccae0` | `e2 03 01 aa` | mov x2,x1 | `FALL_THROUGH`
<a id="insn-00bccae4"></a> `00bccae4` | `21 f9 43 f9` | ldr x1,[x9, #0x7f0] | `FALL_THROUGH`
<a id="insn-00bccae8"></a> `00bccae8` | `08 5d 43 f9` | ldr x8,[x8, #0x6b8] | `FALL_THROUGH`
<a id="insn-00bccaec"></a> `00bccaec` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bccaf0"></a> `00bccaf0` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bccaf4"></a> `00bccaf4` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00bccaf8"></a> `00bccaf8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bccafc"></a> `00bccafc` | `19 39 02 94` | bl 0x00c5af60 | `UNCONDITIONAL_CALL`
<a id="insn-00bccb00"></a> `00bccb00` | `9f 02 00 71` | cmp w20,#0x0 | `FALL_THROUGH`
<a id="insn-00bccb04"></a> `00bccb04` | `e0 17 9f 1a` | cset w0,eq | `FALL_THROUGH`
<a id="insn-00bccb08"></a> `00bccb08` | `a0 e2 1f 39` | strb w0,[x21, #0x7f8] | `FALL_THROUGH`
<a id="insn-00bccb0c"></a> `00bccb0c` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bccb10"></a> `00bccb10` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bccb14"></a> `00bccb14` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bccb18"></a> `00bccb18` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bccab0`](#insn-00bccab0) 範囲 `[['00bccab0', '00bccacb']]`
  - `CONDITIONAL_JUMP` [`00bccac8`](#insn-00bccac8) → [`00bccad4`](#insn-00bccad4)
  - `FALL_THROUGH` [`00bccac8`](#insn-00bccac8) → [`00bccacc`](#insn-00bccacc)
- ブロック [`00bccacc`](#insn-00bccacc) 範囲 `[['00bccacc', '00bccad3']]`
  - `UNCONDITIONAL_JUMP` [`00bccad0`](#insn-00bccad0) → [`00bccb0c`](#insn-00bccb0c)
- ブロック [`00bccad4`](#insn-00bccad4) 範囲 `[['00bccad4', '00bccaef']]`
  - `FALL_THROUGH` [`00bccaec`](#insn-00bccaec) → [`00bccaf0`](#insn-00bccaf0)
- ブロック [`00bccaf0`](#insn-00bccaf0) 範囲 `[['00bccaf0', '00bccb07']]`
  - `FALL_THROUGH` [`00bccb04`](#insn-00bccb04) → [`00bccb08`](#insn-00bccb08)
- ブロック [`00bccb08`](#insn-00bccb08) 範囲 `[['00bccb08', '00bccb0b']]`
  - `FALL_THROUGH` [`00bccb08`](#insn-00bccb08) → [`00bccb0c`](#insn-00bccb0c)
- ブロック [`00bccb0c`](#insn-00bccb0c) 範囲 `[['00bccb0c', '00bccb1b']]`

## 命令位置別の参照

- [`00bccab0`](#insn-00bccab0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bccab4`](#insn-00bccab4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bccab8`](#insn-00bccab8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bccac4`](#insn-00bccac4) → `011267f8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bccac8`](#insn-00bccac8) → [`00bccad4`](#insn-00bccad4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bccad0`](#insn-00bccad0) → [`00bccb0c`](#insn-00bccb0c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bccae4`](#insn-00bccae4) → `011267f0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bccafc`](#insn-00bccafc) → [`00c5af60`](../00c5a/00c5af60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5af60` · 推定シンボル `None` · 推定型 `None`
- [`00bccb08`](#insn-00bccb08) → `011267f8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bccb0c`](#insn-00bccb0c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bccb10`](#insn-00bccb10) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bccab0`](#insn-00bccab0)

~~~json
{
  "source": "00bccab0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bccab4`](#insn-00bccab4)

~~~json
{
  "source": "00bccab4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bccab8`](#insn-00bccab8)

~~~json
{
  "source": "00bccab8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bccac4`](#insn-00bccac4)

~~~json
{
  "source": "00bccac4",
  "target": "011267f8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011267f8",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bccac8`](#insn-00bccac8)

~~~json
{
  "source": "00bccac8",
  "target": "00bccad4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bccad0`](#insn-00bccad0)

~~~json
{
  "source": "00bccad0",
  "target": "00bccb0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bccae4`](#insn-00bccae4)

~~~json
{
  "source": "00bccae4",
  "target": "011267f0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011267f0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bccafc`](#insn-00bccafc)

~~~json
{
  "source": "00bccafc",
  "target": "00c5af60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bccb08`](#insn-00bccb08)

~~~json
{
  "source": "00bccb08",
  "target": "011267f8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011267f8",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bccb0c`](#insn-00bccb0c)

~~~json
{
  "source": "00bccb0c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bccb10`](#insn-00bccb10)

~~~json
{
  "source": "00bccb10",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
