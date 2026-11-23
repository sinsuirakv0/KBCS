# 00b4aacc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00b4ab94`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4a/00b4ab94.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/alignment_unresolved-0004.md#compare-e6ffef8534a51dd7010a9d9248d0c015)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b4aacc",
  "name": "_ZN8firebase9messaging18firebase_messaging10CacheClassEP7_JNIEnvP8_jobject",
  "size": 68,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b344c9721096906b5004fe0d447d2cc2b40e93d44dcceb9c856bbfc6098b2355",
  "source_text_sha256": "b344c9721096906b5004fe0d447d2cc2b40e93d44dcceb9c856bbfc6098b2355",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b4aacc",
        "00b4ab0f"
      ]
    ],
    "bytes_sha256": "a0e7b9994f48476eb61dfc4685ce5c4a8ef9aa1b093202ce7de65cde8aa876d4",
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

- [00bddf90](../00bdd/00bddf90.md)

## 関連文字列（未確認候補）

~~~text
"%PG%com/google/firebase/messaging/FirebaseMessaging"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 763 bytes

~~~c

long _ZN8firebase9messaging18firebase_messaging10CacheClassEP7_JNIEnvP8_jobject
               (undefined8 param_1,undefined8 param_2)

{
                    /* try { // try from 00b4aae0 to 00c4aaeb has its CatchHandler @ 00b4ac38 */
  if (DAT_010a0ef8 == 0) {
                    /* try { // try from 00b4aaec to 00c4ab0b has its CatchHandler @ 00b4ace8 */
    DAT_010a0ef8 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,"com/google/firebase/messaging/FirebaseMessaging",0)
    ;
  }
                    /* try { // try from 00b4ab0c to 00c4ab27 has its CatchHandler @ 00b4acdc */
  return DAT_010a0ef8;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00b4aacc"></a> `00b4aacc` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00b4aad0"></a> `00b4aad0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b4aad4"></a> `00b4aad4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00b4aad8"></a> `00b4aad8` | `b3 2a 00 d0` | adrp x19,0x10a0000 | `FALL_THROUGH`
<a id="insn-00b4aadc"></a> `00b4aadc` | `68 7e 47 f9` | ldr x8,[x19, #0xef8] | `FALL_THROUGH`
<a id="insn-00b4aae0"></a> `00b4aae0` | `08 01 00 b5` | cbnz x8,0x00b4ab00 | `CONDITIONAL_JUMP`
<a id="insn-00b4aae4"></a> `00b4aae4` | `03 bb ff 90` | adrp x3,0x2aa000 | `FALL_THROUGH`
<a id="insn-00b4aae8"></a> `00b4aae8` | `63 70 03 91` | add x3,x3,#0xdc | `FALL_THROUGH`
<a id="insn-00b4aaec"></a> `00b4aaec` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00b4aaf0"></a> `00b4aaf0` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00b4aaf4"></a> `00b4aaf4` | `27 4d 02 94` | bl 0x00bddf90 | `UNCONDITIONAL_CALL`
<a id="insn-00b4aaf8"></a> `00b4aaf8` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00b4aafc"></a> `00b4aafc` | `60 7e 07 f9` | str x0,[x19, #0xef8] | `FALL_THROUGH`
<a id="insn-00b4ab00"></a> `00b4ab00` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b4ab04"></a> `00b4ab04` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00b4ab08"></a> `00b4ab08` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00b4ab0c"></a> `00b4ab0c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00b4aacc`](#insn-00b4aacc) 範囲 `[['00b4aacc', '00b4aadf']]`
  - `FALL_THROUGH` [`00b4aadc`](#insn-00b4aadc) → [`00b4aae0`](#insn-00b4aae0)
- ブロック [`00b4aae0`](#insn-00b4aae0) 範囲 `[['00b4aae0', '00b4aae3']]`
  - `CONDITIONAL_JUMP` [`00b4aae0`](#insn-00b4aae0) → [`00b4ab00`](#insn-00b4ab00)
  - `FALL_THROUGH` [`00b4aae0`](#insn-00b4aae0) → [`00b4aae4`](#insn-00b4aae4)
- ブロック [`00b4aae4`](#insn-00b4aae4) 範囲 `[['00b4aae4', '00b4aaeb']]`
  - `FALL_THROUGH` [`00b4aae8`](#insn-00b4aae8) → [`00b4aaec`](#insn-00b4aaec)
- ブロック [`00b4aaec`](#insn-00b4aaec) 範囲 `[['00b4aaec', '00b4aaff']]`
  - `FALL_THROUGH` [`00b4aafc`](#insn-00b4aafc) → [`00b4ab00`](#insn-00b4ab00)
- ブロック [`00b4ab00`](#insn-00b4ab00) 範囲 `[['00b4ab00', '00b4ab0b']]`
  - `FALL_THROUGH` [`00b4ab08`](#insn-00b4ab08) → [`00b4ab0c`](#insn-00b4ab0c)
- ブロック [`00b4ab0c`](#insn-00b4ab0c) 範囲 `[['00b4ab0c', '00b4ab0f']]`

## 命令位置別の参照

- [`00b4aacc`](#insn-00b4aacc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4aad0`](#insn-00b4aad0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4aadc`](#insn-00b4aadc) → `010a0ef8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00b4aae0`](#insn-00b4aae0) → [`00b4ab00`](#insn-00b4ab00) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4aae8`](#insn-00b4aae8) → `002aa0dc`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00b4aaf4`](#insn-00b4aaf4) → [`00bddf90`](../00bdd/00bddf90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddf90` · 推定シンボル `None` · 推定型 `None`
- [`00b4aafc`](#insn-00b4aafc) → `010a0ef8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00b4ab00`](#insn-00b4ab00) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b4aacc`](#insn-00b4aacc)

~~~json
{
  "source": "00b4aacc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4aad0`](#insn-00b4aad0)

~~~json
{
  "source": "00b4aad0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4aadc`](#insn-00b4aadc)

~~~json
{
  "source": "00b4aadc",
  "target": "010a0ef8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0ef8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b4aae0`](#insn-00b4aae0)

~~~json
{
  "source": "00b4aae0",
  "target": "00b4ab00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4aae8`](#insn-00b4aae8)

~~~json
{
  "source": "00b4aae8",
  "target": "002aa0dc",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002aa0d8",
  "offset": 4,
  "size": 52,
  "datatype": "string",
  "bytes": "25504725636f6d2f676f6f676c652f66697265626173652f6d6573736167696e",
  "capture_start": "002aa0d8",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00b4aaf4`](#insn-00b4aaf4)

~~~json
{
  "source": "00b4aaf4",
  "target": "00bddf90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b4aafc`](#insn-00b4aafc)

~~~json
{
  "source": "00b4aafc",
  "target": "010a0ef8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0ef8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b4ab00`](#insn-00b4ab00)

~~~json
{
  "source": "00b4ab00",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
