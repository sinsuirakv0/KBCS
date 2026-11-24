# 00bddbfc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bdd7d4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdd7d4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0085.md#compare-2102a80591588720a13980da81211f01)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bddc98`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bddc98.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0085.md#compare-b916ab3be908e251c25844e2d8970296)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bddbfc",
  "name": "_ZN8firebase4auth18userprofilebuilder10CacheClassEP7_JNIEnvP8_jobject",
  "size": 68,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "74c58d7bf106dbafe52c27803c3ac5ddb4a2792a53422ba38de0f6885b41b618",
  "source_text_sha256": "74c58d7bf106dbafe52c27803c3ac5ddb4a2792a53422ba38de0f6885b41b618",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bddbfc",
        "00bddc3f"
      ]
    ],
    "bytes_sha256": "3882620de308f4f0923c782a10b697e28063673ef6b1168242d70ba148f72967",
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

- [00c5af10](../00c5a/00c5af10.md)

## 関連文字列（未確認候補）

~~~text
"%PG%com/google/firebase/auth/UserProfileChangeRequest$Builder"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 503 bytes

~~~c

long _ZN8firebase4auth18userprofilebuilder10CacheClassEP7_JNIEnvP8_jobject
               (undefined8 param_1,undefined8 param_2)

{
  if (DAT_01126e28 == 0) {
    DAT_01126e28 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,
                              "com/google/firebase/auth/UserProfileChangeRequest$Builder",0);
  }
  return DAT_01126e28;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bddbfc"></a> `00bddbfc` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bddc00"></a> `00bddc00` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bddc04"></a> `00bddc04` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bddc08"></a> `00bddc08` | `53 2a 00 b0` | adrp x19,0x1126000 | `FALL_THROUGH`
<a id="insn-00bddc0c"></a> `00bddc0c` | `68 16 47 f9` | ldr x8,[x19, #0xe28] | `FALL_THROUGH`
<a id="insn-00bddc10"></a> `00bddc10` | `08 01 00 b5` | cbnz x8,0x00bddc30 | `CONDITIONAL_JUMP`
<a id="insn-00bddc14"></a> `00bddc14` | `83 b6 ff 90` | adrp x3,0x2ad000 | `FALL_THROUGH`
<a id="insn-00bddc18"></a> `00bddc18` | `63 20 12 91` | add x3,x3,#0x488 | `FALL_THROUGH`
<a id="insn-00bddc1c"></a> `00bddc1c` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00bddc20"></a> `00bddc20` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00bddc24"></a> `00bddc24` | `bb f4 01 94` | bl 0x00c5af10 | `UNCONDITIONAL_CALL`
<a id="insn-00bddc28"></a> `00bddc28` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00bddc2c"></a> `00bddc2c` | `60 16 07 f9` | str x0,[x19, #0xe28] | `FALL_THROUGH`
<a id="insn-00bddc30"></a> `00bddc30` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bddc34"></a> `00bddc34` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00bddc38"></a> `00bddc38` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bddc3c"></a> `00bddc3c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bddbfc`](#insn-00bddbfc) 範囲 `[['00bddbfc', '00bddc13']]`
  - `CONDITIONAL_JUMP` [`00bddc10`](#insn-00bddc10) → [`00bddc30`](#insn-00bddc30)
  - `FALL_THROUGH` [`00bddc10`](#insn-00bddc10) → [`00bddc14`](#insn-00bddc14)
- ブロック [`00bddc14`](#insn-00bddc14) 範囲 `[['00bddc14', '00bddc2f']]`
  - `FALL_THROUGH` [`00bddc2c`](#insn-00bddc2c) → [`00bddc30`](#insn-00bddc30)
- ブロック [`00bddc30`](#insn-00bddc30) 範囲 `[['00bddc30', '00bddc3f']]`

## 命令位置別の参照

- [`00bddbfc`](#insn-00bddbfc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bddc00`](#insn-00bddc00) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bddc0c`](#insn-00bddc0c) → `01126e28`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bddc10`](#insn-00bddc10) → [`00bddc30`](#insn-00bddc30) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bddc18`](#insn-00bddc18) → `002ad488`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bddc24`](#insn-00bddc24) → [`00c5af10`](../00c5a/00c5af10.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5af10` · 推定シンボル `None` · 推定型 `None`
- [`00bddc2c`](#insn-00bddc2c) → `01126e28`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bddc30`](#insn-00bddc30) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bddbfc`](#insn-00bddbfc)

~~~json
{
  "source": "00bddbfc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bddc00`](#insn-00bddc00)

~~~json
{
  "source": "00bddc00",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bddc0c`](#insn-00bddc0c)

~~~json
{
  "source": "00bddc0c",
  "target": "01126e28",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126e28",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bddc10`](#insn-00bddc10)

~~~json
{
  "source": "00bddc10",
  "target": "00bddc30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bddc18`](#insn-00bddc18)

~~~json
{
  "source": "00bddc18",
  "target": "002ad488",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002ad484",
  "offset": 4,
  "size": 62,
  "datatype": "string",
  "bytes": "25504725636f6d2f676f6f676c652f66697265626173652f617574682f557365",
  "capture_start": "002ad484",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bddc24`](#insn-00bddc24)

~~~json
{
  "source": "00bddc24",
  "target": "00c5af10",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bddc2c`](#insn-00bddc2c)

~~~json
{
  "source": "00bddc2c",
  "target": "01126e28",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126e28",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bddc30`](#insn-00bddc30)

~~~json
{
  "source": "00bddc30",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
