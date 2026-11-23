# 00aebb5c

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00aeba94`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aeb/00aeba94.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0060.md#compare-3f903398f9ed818c9c61b9de4fec34fd)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00aebba0`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aebba0.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0064.md#compare-e9dce1394f1f23555a981b5886c81af7)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aebb5c",
  "name": "_ZN8firebase4util8iterator19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "fc6538a1027d776a5bc7be39d2af4a9876745c7bb3586e1318b6af244b50efe1",
  "source_text_sha256": "fc6538a1027d776a5bc7be39d2af4a9876745c7bb3586e1318b6af244b50efe1",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aebb5c",
        "00aebb9b"
      ]
    ],
    "bytes_sha256": "4759783d3d6250f075d7efc59e1cc60aad0f673f0fd44f2d7a10e48aa6578a87",
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

- [00bde040](../00bde/00bde040.md)

## 関連文字列（未確認候補）

~~~text
"java/util/Iterator"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 427 bytes

~~~c

long _ZN8firebase4util8iterator19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE
               (void)

{
  if (DAT_010a08b8 == 0) {
    DAT_010a08b8 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             ();
  }
  return DAT_010a08b8;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aebb5c"></a> `00aebb5c` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00aebb60"></a> `00aebb60` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aebb64"></a> `00aebb64` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00aebb68"></a> `00aebb68` | `b3 2d 00 b0` | adrp x19,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aebb6c"></a> `00aebb6c` | `68 5e 44 f9` | ldr x8,[x19, #0x8b8] | `FALL_THROUGH`
<a id="insn-00aebb70"></a> `00aebb70` | `e8 00 00 b5` | cbnz x8,0x00aebb8c | `CONDITIONAL_JUMP`
<a id="insn-00aebb74"></a> `00aebb74` | `63 bd ff 90` | adrp x3,0x297000 | `FALL_THROUGH`
<a id="insn-00aebb78"></a> `00aebb78` | `63 9c 15 91` | add x3,x3,#0x567 | `FALL_THROUGH`
<a id="insn-00aebb7c"></a> `00aebb7c` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00aebb80"></a> `00aebb80` | `30 c9 03 94` | bl 0x00bde040 | `UNCONDITIONAL_CALL`
<a id="insn-00aebb84"></a> `00aebb84` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00aebb88"></a> `00aebb88` | `60 5e 04 f9` | str x0,[x19, #0x8b8] | `FALL_THROUGH`
<a id="insn-00aebb8c"></a> `00aebb8c` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aebb90"></a> `00aebb90` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00aebb94"></a> `00aebb94` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00aebb98"></a> `00aebb98` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aebb5c`](#insn-00aebb5c) 範囲 `[['00aebb5c', '00aebb73']]`
  - `CONDITIONAL_JUMP` [`00aebb70`](#insn-00aebb70) → [`00aebb8c`](#insn-00aebb8c)
  - `FALL_THROUGH` [`00aebb70`](#insn-00aebb70) → [`00aebb74`](#insn-00aebb74)
- ブロック [`00aebb74`](#insn-00aebb74) 範囲 `[['00aebb74', '00aebb8b']]`
  - `FALL_THROUGH` [`00aebb88`](#insn-00aebb88) → [`00aebb8c`](#insn-00aebb8c)
- ブロック [`00aebb8c`](#insn-00aebb8c) 範囲 `[['00aebb8c', '00aebb9b']]`

## 命令位置別の参照

- [`00aebb5c`](#insn-00aebb5c) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aebb60`](#insn-00aebb60) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aebb6c`](#insn-00aebb6c) → `010a08b8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aebb70`](#insn-00aebb70) → [`00aebb8c`](#insn-00aebb8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aebb78`](#insn-00aebb78) → `00297567`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aebb80`](#insn-00aebb80) → [`00bde040`](../00bde/00bde040.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde040` · 推定シンボル `None` · 推定型 `None`
- [`00aebb88`](#insn-00aebb88) → `010a08b8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aebb8c`](#insn-00aebb8c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aebb5c`](#insn-00aebb5c)

~~~json
{
  "source": "00aebb5c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aebb60`](#insn-00aebb60)

~~~json
{
  "source": "00aebb60",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aebb6c`](#insn-00aebb6c)

~~~json
{
  "source": "00aebb6c",
  "target": "010a08b8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a08b8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aebb70`](#insn-00aebb70)

~~~json
{
  "source": "00aebb70",
  "target": "00aebb8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aebb78`](#insn-00aebb78)

~~~json
{
  "source": "00aebb78",
  "target": "00297567",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00297567",
  "offset": 0,
  "size": 19,
  "datatype": "string",
  "bytes": "6a6176612f7574696c2f4974657261746f7200",
  "capture_start": "00297567",
  "capture_bytes": 19,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aebb80`](#insn-00aebb80)

~~~json
{
  "source": "00aebb80",
  "target": "00bde040",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aebb88`](#insn-00aebb88)

~~~json
{
  "source": "00aebb88",
  "target": "010a08b8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a08b8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aebb8c`](#insn-00aebb8c)

~~~json
{
  "source": "00aebb8c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
