# 00aebbe0

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00aebb9c`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aebb9c.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0064.md#compare-3b70fd148556fff08870f85f15566141)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00b4b964`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4b964.md) · 移動量 `+0x5fd84`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0058.md#compare-a4b8d49bc66c9e3206b381978df130a9)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aebbe0",
  "name": "_ZN8firebase4util8iterator10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE",
  "size": 68,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "af22e2f4222f704d323b77d35434a5616f55572928b8d775ef4dc1a5762edf52",
  "source_text_sha256": "af22e2f4222f704d323b77d35434a5616f55572928b8d775ef4dc1a5762edf52",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aebbe0",
        "00aebc23"
      ]
    ],
    "bytes_sha256": "930bf4a33ac43b17a4689b845cf7bf9ac800daf5d24ac415c7d987f516cd3f78",
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

- [00bde090](../00bde/00bde090.md)

## 関連文字列（未確認候補）

~~~text
"java/util/Iterator"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 567 bytes

~~~c

long _ZN8firebase4util8iterator10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE
               (undefined8 param_1,undefined8 param_2,undefined4 param_3)

{
  if (DAT_010a08f8 == 0) {
                    /* try { // try from 00aebc08 to 00bebc1f has its CatchHandler @ 00af1ad0 */
    DAT_010a08f8 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,"java/util/Iterator",param_3);
  }
  return DAT_010a08f8;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aebbe0"></a> `00aebbe0` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00aebbe4"></a> `00aebbe4` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aebbe8"></a> `00aebbe8` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00aebbec"></a> `00aebbec` | `b3 2d 00 b0` | adrp x19,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aebbf0"></a> `00aebbf0` | `68 7e 44 f9` | ldr x8,[x19, #0x8f8] | `FALL_THROUGH`
<a id="insn-00aebbf4"></a> `00aebbf4` | `08 01 00 b5` | cbnz x8,0x00aebc14 | `CONDITIONAL_JUMP`
<a id="insn-00aebbf8"></a> `00aebbf8` | `63 bd ff 90` | adrp x3,0x297000 | `FALL_THROUGH`
<a id="insn-00aebbfc"></a> `00aebbfc` | `e4 03 02 2a` | mov w4,w2 | `FALL_THROUGH`
<a id="insn-00aebc00"></a> `00aebc00` | `63 68 13 91` | add x3,x3,#0x4da | `FALL_THROUGH`
<a id="insn-00aebc04"></a> `00aebc04` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00aebc08"></a> `00aebc08` | `22 c9 03 94` | bl 0x00bde090 | `UNCONDITIONAL_CALL`
<a id="insn-00aebc0c"></a> `00aebc0c` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00aebc10"></a> `00aebc10` | `60 7e 04 f9` | str x0,[x19, #0x8f8] | `FALL_THROUGH`
<a id="insn-00aebc14"></a> `00aebc14` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aebc18"></a> `00aebc18` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00aebc1c"></a> `00aebc1c` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00aebc20"></a> `00aebc20` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aebbe0`](#insn-00aebbe0) 範囲 `[['00aebbe0', '00aebbf7']]`
  - `CONDITIONAL_JUMP` [`00aebbf4`](#insn-00aebbf4) → [`00aebc14`](#insn-00aebc14)
  - `FALL_THROUGH` [`00aebbf4`](#insn-00aebbf4) → [`00aebbf8`](#insn-00aebbf8)
- ブロック [`00aebbf8`](#insn-00aebbf8) 範囲 `[['00aebbf8', '00aebc07']]`
  - `FALL_THROUGH` [`00aebc04`](#insn-00aebc04) → [`00aebc08`](#insn-00aebc08)
- ブロック [`00aebc08`](#insn-00aebc08) 範囲 `[['00aebc08', '00aebc13']]`
  - `FALL_THROUGH` [`00aebc10`](#insn-00aebc10) → [`00aebc14`](#insn-00aebc14)
- ブロック [`00aebc14`](#insn-00aebc14) 範囲 `[['00aebc14', '00aebc23']]`

## 命令位置別の参照

- [`00aebbe0`](#insn-00aebbe0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aebbe4`](#insn-00aebbe4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aebbf0`](#insn-00aebbf0) → `010a08f8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aebbf4`](#insn-00aebbf4) → [`00aebc14`](#insn-00aebc14) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aebc00`](#insn-00aebc00) → `002974da`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aebc08`](#insn-00aebc08) → [`00bde090`](../00bde/00bde090.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde090` · 推定シンボル `None` · 推定型 `None`
- [`00aebc10`](#insn-00aebc10) → `010a08f8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aebc14`](#insn-00aebc14) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aebbe0`](#insn-00aebbe0)

~~~json
{
  "source": "00aebbe0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aebbe4`](#insn-00aebbe4)

~~~json
{
  "source": "00aebbe4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aebbf0`](#insn-00aebbf0)

~~~json
{
  "source": "00aebbf0",
  "target": "010a08f8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a08f8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aebbf4`](#insn-00aebbf4)

~~~json
{
  "source": "00aebbf4",
  "target": "00aebc14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aebc00`](#insn-00aebc00)

~~~json
{
  "source": "00aebc00",
  "target": "002974da",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002974da",
  "offset": 0,
  "size": 19,
  "datatype": "string",
  "bytes": "6a6176612f7574696c2f4974657261746f7200",
  "capture_start": "002974da",
  "capture_bytes": 19,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aebc08`](#insn-00aebc08)

~~~json
{
  "source": "00aebc08",
  "target": "00bde090",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aebc10`](#insn-00aebc10)

~~~json
{
  "source": "00aebc10",
  "target": "010a08f8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a08f8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aebc14`](#insn-00aebc14)

~~~json
{
  "source": "00aebc14",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
