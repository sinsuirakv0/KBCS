# 00aecda8

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00aecd64`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aecd64.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0064.md#compare-b0e1944ac641538c36a43643a57757dd)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00b4cb2c`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4cb2c.md) · 移動量 `+0x5fd84`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0059.md#compare-6c0d55da66137f1df26efb045d88bbda)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aecda8",
  "name": "_ZN8firebase4util3set19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0_16ClassRequirementE",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "8d54a48de65d49f7695b9896788364acb061d4a6519e7343cff7a2254d30619e",
  "source_text_sha256": "8d54a48de65d49f7695b9896788364acb061d4a6519e7343cff7a2254d30619e",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aecda8",
        "00aecde7"
      ]
    ],
    "bytes_sha256": "da583a939d817c088859cdef29c3a964d9fcfccd6d3e50148b00cbff9cf06c52",
    "instruction_count": 16,
    "instruction_bytes": 64,
    "body_bytes": 64,
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
"java/util/Set"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 445 bytes

~~~c

long _ZN8firebase4util3set19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0_16ClassRequirementE
               (void)

{
  if (DAT_010a09c8 == 0) {
    DAT_010a09c8 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             ();
  }
  return DAT_010a09c8;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aecda8"></a> `00aecda8` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00aecdac"></a> `00aecdac` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aecdb0"></a> `00aecdb0` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00aecdb4"></a> `00aecdb4` | `b3 2d 00 90` | adrp x19,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aecdb8"></a> `00aecdb8` | `68 e6 44 f9` | ldr x8,[x19, #0x9c8] | `FALL_THROUGH`
<a id="insn-00aecdbc"></a> `00aecdbc` | `e8 00 00 b5` | cbnz x8,0x00aecdd8 | `CONDITIONAL_JUMP`
<a id="insn-00aecdc0"></a> `00aecdc0` | `e4 03 03 2a` | mov w4,w3 | `FALL_THROUGH`
<a id="insn-00aecdc4"></a> `00aecdc4` | `a3 bd ff 90` | adrp x3,0x2a0000 | `FALL_THROUGH`
<a id="insn-00aecdc8"></a> `00aecdc8` | `63 28 01 91` | add x3,x3,#0x4a | `FALL_THROUGH`
<a id="insn-00aecdcc"></a> `00aecdcc` | `b1 c4 03 94` | bl 0x00bde090 | `UNCONDITIONAL_CALL`
<a id="insn-00aecdd0"></a> `00aecdd0` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00aecdd4"></a> `00aecdd4` | `60 e6 04 f9` | str x0,[x19, #0x9c8] | `FALL_THROUGH`
<a id="insn-00aecdd8"></a> `00aecdd8` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aecddc"></a> `00aecddc` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00aecde0"></a> `00aecde0` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00aecde4"></a> `00aecde4` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aecda8`](#insn-00aecda8) 範囲 `[['00aecda8', '00aecdbf']]`
  - `CONDITIONAL_JUMP` [`00aecdbc`](#insn-00aecdbc) → [`00aecdd8`](#insn-00aecdd8)
  - `FALL_THROUGH` [`00aecdbc`](#insn-00aecdbc) → [`00aecdc0`](#insn-00aecdc0)
- ブロック [`00aecdc0`](#insn-00aecdc0) 範囲 `[['00aecdc0', '00aecdd7']]`
  - `FALL_THROUGH` [`00aecdd4`](#insn-00aecdd4) → [`00aecdd8`](#insn-00aecdd8)
- ブロック [`00aecdd8`](#insn-00aecdd8) 範囲 `[['00aecdd8', '00aecde7']]`

## 命令位置別の参照

- [`00aecda8`](#insn-00aecda8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aecdac`](#insn-00aecdac) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aecdb8`](#insn-00aecdb8) → `010a09c8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aecdbc`](#insn-00aecdbc) → [`00aecdd8`](#insn-00aecdd8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aecdc8`](#insn-00aecdc8) → `002a004a`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aecdcc`](#insn-00aecdcc) → [`00bde090`](../00bde/00bde090.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde090` · 推定シンボル `None` · 推定型 `None`
- [`00aecdd4`](#insn-00aecdd4) → `010a09c8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aecdd8`](#insn-00aecdd8) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aecda8`](#insn-00aecda8)

~~~json
{
  "source": "00aecda8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aecdac`](#insn-00aecdac)

~~~json
{
  "source": "00aecdac",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aecdb8`](#insn-00aecdb8)

~~~json
{
  "source": "00aecdb8",
  "target": "010a09c8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a09c8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aecdbc`](#insn-00aecdbc)

~~~json
{
  "source": "00aecdbc",
  "target": "00aecdd8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aecdc8`](#insn-00aecdc8)

~~~json
{
  "source": "00aecdc8",
  "target": "002a004a",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a004a",
  "offset": 0,
  "size": 14,
  "datatype": "string",
  "bytes": "6a6176612f7574696c2f53657400",
  "capture_start": "002a004a",
  "capture_bytes": 14,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aecdcc`](#insn-00aecdcc)

~~~json
{
  "source": "00aecdcc",
  "target": "00bde090",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aecdd4`](#insn-00aecdd4)

~~~json
{
  "source": "00aecdd4",
  "target": "010a09c8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a09c8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aecdd8`](#insn-00aecdd8)

~~~json
{
  "source": "00aecdd8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
