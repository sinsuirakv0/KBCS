# 00bccce4

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bcc8bc`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc8bc.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0081.md#compare-c221feea69953019f3d4b21a8099eefb)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bccd80`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcc/00bccd80.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0081.md#compare-1a4c605f46b5f4897e5195c5e611675f)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bccce4",
  "name": "_ZN8firebase4auth21jni_id_token_listener19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS_4util16ClassRequirementE",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "edb8b7c8ef3d0b203ea385f50759274a5291635e746d963c52e1eb52f28c4659",
  "source_text_sha256": "edb8b7c8ef3d0b203ea385f50759274a5291635e746d963c52e1eb52f28c4659",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bccce4",
        "00bccd23"
      ]
    ],
    "bytes_sha256": "32cbfa92d6b5e351a2ce2464fe5614a9e85b75aa4fe8429ae093d6dca30b106b",
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

- [00c5af10](../00c5a/00c5af10.md)

## 関連文字列（未確認候補）

~~~text
"com/google/firebase/auth/internal/cpp/JniIdTokenListener"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 662 bytes

~~~c

long _ZN8firebase4auth21jni_id_token_listener19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS_4util16ClassRequirementE
               (void)

{
  if (DAT_01126818 == 0) {
                    /* try { // try from 00bccd00 to 00cccd17 has its CatchHandler @ 00bce8fc */
    DAT_01126818 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             ();
  }
                    /* try { // try from 00bccd18 to 00cccdcb has its CatchHandler @ 00bcc5d0 */
  return DAT_01126818;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bccce4"></a> `00bccce4` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bccce8"></a> `00bccce8` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcccec"></a> `00bcccec` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bcccf0"></a> `00bcccf0` | `d3 2a 00 d0` | adrp x19,0x1126000 | `FALL_THROUGH`
<a id="insn-00bcccf4"></a> `00bcccf4` | `68 0e 44 f9` | ldr x8,[x19, #0x818] | `FALL_THROUGH`
<a id="insn-00bcccf8"></a> `00bcccf8` | `e8 00 00 b5` | cbnz x8,0x00bccd14 | `CONDITIONAL_JUMP`
<a id="insn-00bcccfc"></a> `00bcccfc` | `e4 03 03 2a` | mov w4,w3 | `FALL_THROUGH`
<a id="insn-00bccd00"></a> `00bccd00` | `e3 b6 ff d0` | adrp x3,0x2aa000 | `FALL_THROUGH`
<a id="insn-00bccd04"></a> `00bccd04` | `63 28 26 91` | add x3,x3,#0x98a | `FALL_THROUGH`
<a id="insn-00bccd08"></a> `00bccd08` | `82 38 02 94` | bl 0x00c5af10 | `UNCONDITIONAL_CALL`
<a id="insn-00bccd0c"></a> `00bccd0c` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00bccd10"></a> `00bccd10` | `60 0e 04 f9` | str x0,[x19, #0x818] | `FALL_THROUGH`
<a id="insn-00bccd14"></a> `00bccd14` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bccd18"></a> `00bccd18` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00bccd1c"></a> `00bccd1c` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bccd20"></a> `00bccd20` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bccce4`](#insn-00bccce4) 範囲 `[['00bccce4', '00bcccfb']]`
  - `CONDITIONAL_JUMP` [`00bcccf8`](#insn-00bcccf8) → [`00bccd14`](#insn-00bccd14)
  - `FALL_THROUGH` [`00bcccf8`](#insn-00bcccf8) → [`00bcccfc`](#insn-00bcccfc)
- ブロック [`00bcccfc`](#insn-00bcccfc) 範囲 `[['00bcccfc', '00bcccff']]`
  - `FALL_THROUGH` [`00bcccfc`](#insn-00bcccfc) → [`00bccd00`](#insn-00bccd00)
- ブロック [`00bccd00`](#insn-00bccd00) 範囲 `[['00bccd00', '00bccd13']]`
  - `FALL_THROUGH` [`00bccd10`](#insn-00bccd10) → [`00bccd14`](#insn-00bccd14)
- ブロック [`00bccd14`](#insn-00bccd14) 範囲 `[['00bccd14', '00bccd17']]`
  - `FALL_THROUGH` [`00bccd14`](#insn-00bccd14) → [`00bccd18`](#insn-00bccd18)
- ブロック [`00bccd18`](#insn-00bccd18) 範囲 `[['00bccd18', '00bccd23']]`

## 命令位置別の参照

- [`00bccce4`](#insn-00bccce4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bccce8`](#insn-00bccce8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcccf4`](#insn-00bcccf4) → `01126818`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bcccf8`](#insn-00bcccf8) → [`00bccd14`](#insn-00bccd14) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bccd04`](#insn-00bccd04) → `002aa98a`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bccd08`](#insn-00bccd08) → [`00c5af10`](../00c5a/00c5af10.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5af10` · 推定シンボル `None` · 推定型 `None`
- [`00bccd10`](#insn-00bccd10) → `01126818`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bccd14`](#insn-00bccd14) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bccce4`](#insn-00bccce4)

~~~json
{
  "source": "00bccce4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bccce8`](#insn-00bccce8)

~~~json
{
  "source": "00bccce8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcccf4`](#insn-00bcccf4)

~~~json
{
  "source": "00bcccf4",
  "target": "01126818",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126818",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bcccf8`](#insn-00bcccf8)

~~~json
{
  "source": "00bcccf8",
  "target": "00bccd14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bccd04`](#insn-00bccd04)

~~~json
{
  "source": "00bccd04",
  "target": "002aa98a",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002aa98a",
  "offset": 0,
  "size": 57,
  "datatype": "string",
  "bytes": "636f6d2f676f6f676c652f66697265626173652f617574682f696e7465726e61",
  "capture_start": "002aa98a",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bccd08`](#insn-00bccd08)

~~~json
{
  "source": "00bccd08",
  "target": "00c5af10",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bccd10`](#insn-00bccd10)

~~~json
{
  "source": "00bccd10",
  "target": "01126818",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126818",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bccd14`](#insn-00bccd14)

~~~json
{
  "source": "00bccd14",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
