# 00aedcc8

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00aedc00`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aedc00.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0061.md#compare-cb5e3c8676600fc6fc26f55f980ced16)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00aedd0c`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aedd0c.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0065.md#compare-ed3d196d44faf28b9bbd930c1ee7360b)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aedcc8",
  "name": "_ZN8firebase4util3uri10CacheClassEP7_JNIEnvP8_jobject",
  "size": 68,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "7df24a71ba2c66c0c9d9b81b9ef6476135bec86061e16062fa774439a0d44dbf",
  "source_text_sha256": "7df24a71ba2c66c0c9d9b81b9ef6476135bec86061e16062fa774439a0d44dbf",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aedcc8",
        "00aedd0b"
      ]
    ],
    "bytes_sha256": "54c2c9900a3c53d16555ac95287d459543a51a785d141eae7745c2eae352550b",
    "instruction_count": 17,
    "instruction_bytes": 68,
    "body_bytes": 68,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bde040](../00bde/00bde040.md)

## 関連文字列（未確認候補）

~~~text
"android/net/Uri"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 398 bytes

~~~c

long _ZN8firebase4util3uri10CacheClassEP7_JNIEnvP8_jobject(undefined8 param_1,undefined8 param_2)

{
  if (DAT_010a0a20 == 0) {
    DAT_010a0a20 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,"android/net/Uri",0);
  }
  return DAT_010a0a20;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aedcc8"></a> `00aedcc8` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00aedccc"></a> `00aedccc` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aedcd0"></a> `00aedcd0` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00aedcd4"></a> `00aedcd4` | `93 2d 00 f0` | adrp x19,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aedcd8"></a> `00aedcd8` | `68 12 45 f9` | ldr x8,[x19, #0xa20] | `FALL_THROUGH`
<a id="insn-00aedcdc"></a> `00aedcdc` | `08 01 00 b5` | cbnz x8,0x00aedcfc | `CONDITIONAL_JUMP`
<a id="insn-00aedce0"></a> `00aedce0` | `43 bd ff d0` | adrp x3,0x297000 | `FALL_THROUGH`
<a id="insn-00aedce4"></a> `00aedce4` | `63 14 16 91` | add x3,x3,#0x585 | `FALL_THROUGH`
<a id="insn-00aedce8"></a> `00aedce8` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00aedcec"></a> `00aedcec` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00aedcf0"></a> `00aedcf0` | `d4 c0 03 94` | bl 0x00bde040 | `UNCONDITIONAL_CALL`
<a id="insn-00aedcf4"></a> `00aedcf4` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00aedcf8"></a> `00aedcf8` | `60 12 05 f9` | str x0,[x19, #0xa20] | `FALL_THROUGH`
<a id="insn-00aedcfc"></a> `00aedcfc` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aedd00"></a> `00aedd00` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00aedd04"></a> `00aedd04` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00aedd08"></a> `00aedd08` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aedcc8`](#insn-00aedcc8) 範囲 `[['00aedcc8', '00aedcdf']]`
  - `CONDITIONAL_JUMP` [`00aedcdc`](#insn-00aedcdc) → [`00aedcfc`](#insn-00aedcfc)
  - `FALL_THROUGH` [`00aedcdc`](#insn-00aedcdc) → [`00aedce0`](#insn-00aedce0)
- ブロック [`00aedce0`](#insn-00aedce0) 範囲 `[['00aedce0', '00aedcfb']]`
  - `FALL_THROUGH` [`00aedcf8`](#insn-00aedcf8) → [`00aedcfc`](#insn-00aedcfc)
- ブロック [`00aedcfc`](#insn-00aedcfc) 範囲 `[['00aedcfc', '00aedd0b']]`

## 命令位置別の参照

- [`00aedcc8`](#insn-00aedcc8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aedccc`](#insn-00aedccc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aedcd8`](#insn-00aedcd8) → `010a0a20`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aedcdc`](#insn-00aedcdc) → [`00aedcfc`](#insn-00aedcfc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aedce4`](#insn-00aedce4) → `00297585`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aedcf0`](#insn-00aedcf0) → [`00bde040`](../00bde/00bde040.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde040` · 推定シンボル `None` · 推定型 `None`
- [`00aedcf8`](#insn-00aedcf8) → `010a0a20`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aedcfc`](#insn-00aedcfc) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aedcc8`](#insn-00aedcc8)

~~~json
{
  "source": "00aedcc8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aedccc`](#insn-00aedccc)

~~~json
{
  "source": "00aedccc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aedcd8`](#insn-00aedcd8)

~~~json
{
  "source": "00aedcd8",
  "target": "010a0a20",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0a20",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aedcdc`](#insn-00aedcdc)

~~~json
{
  "source": "00aedcdc",
  "target": "00aedcfc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aedce4`](#insn-00aedce4)

~~~json
{
  "source": "00aedce4",
  "target": "00297585",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00297585",
  "offset": 0,
  "size": 16,
  "datatype": "string",
  "bytes": "616e64726f69642f6e65742f55726900",
  "capture_start": "00297585",
  "capture_bytes": 16,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aedcf0`](#insn-00aedcf0)

~~~json
{
  "source": "00aedcf0",
  "target": "00bde040",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aedcf8`](#insn-00aedcf8)

~~~json
{
  "source": "00aedcf8",
  "target": "010a0a20",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0a20",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aedcfc`](#insn-00aedcfc)

~~~json
{
  "source": "00aedcfc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
