# 00b5ceac

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00b5ce68`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5ce68.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0070.md#compare-7195b91c9cff18aa26b46a82d42c5660)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bcc3ac`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc3ac.md) · 移動量 `+0x6f500`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0066.md#compare-1af1b57bddb23032aa3d5c20e10d9898)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b5ceac",
  "name": "_ZN8firebase4auth17signinmethodquery12ReleaseClassEP7_JNIEnv",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "7191e079b324d53c022b08801d6e96d5f039e97b9f6411b1b91ca0e1c331372a",
  "source_text_sha256": "7191e079b324d53c022b08801d6e96d5f039e97b9f6411b1b91ca0e1c331372a",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b5ceac",
        "00b5cf1b"
      ]
    ],
    "bytes_sha256": "67e7e1cd72a10cd968a1844c4cf3aeb42428e961cdd7f982282cf0854d5330b7",
    "instruction_count": 28,
    "instruction_bytes": 112,
    "body_bytes": 112,
    "indirect": 2,
    "unresolved": 2
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bde0e0](../00bde/00bde0e0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 392 bytes

~~~c

void _ZN8firebase4auth17signinmethodquery12ReleaseClassEP7_JNIEnv(long *param_1)

{
  if (DAT_010a14c8 != 0) {
    if (DAT_010a14d0 != '\0') {
      (**(code **)(*param_1 + 0x6c0))(param_1);
      DAT_010a14d0 = '\0';
    }
    _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(param_1);
    (**(code **)(*param_1 + 0xb0))(param_1,DAT_010a14c8);
    DAT_010a14c8 = 0;
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00b5ceac"></a> `00b5ceac` | `f5 0f 1d f8` | str x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00b5ceb0"></a> `00b5ceb0` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b5ceb4"></a> `00b5ceb4` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b5ceb8"></a> `00b5ceb8` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00b5cebc"></a> `00b5cebc` | `34 2a 00 b0` | adrp x20,0x10a1000 | `FALL_THROUGH`
<a id="insn-00b5cec0"></a> `00b5cec0` | `81 66 42 f9` | ldr x1,[x20, #0x4c8] | `FALL_THROUGH`
<a id="insn-00b5cec4"></a> `00b5cec4` | `41 02 00 b4` | cbz x1,0x00b5cf0c | `CONDITIONAL_JUMP`
<a id="insn-00b5cec8"></a> `00b5cec8` | `35 2a 00 b0` | adrp x21,0x10a1000 | `FALL_THROUGH`
<a id="insn-00b5cecc"></a> `00b5cecc` | `a8 42 53 39` | ldrb w8,[x21, #0x4d0] | `FALL_THROUGH`
<a id="insn-00b5ced0"></a> `00b5ced0` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00b5ced4"></a> `00b5ced4` | `c8 00 00 34` | cbz w8,0x00b5ceec | `CONDITIONAL_JUMP`
<a id="insn-00b5ced8"></a> `00b5ced8` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00b5cedc"></a> `00b5cedc` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b5cee0"></a> `00b5cee0` | `08 61 43 f9` | ldr x8,[x8, #0x6c0] | `FALL_THROUGH`
<a id="insn-00b5cee4"></a> `00b5cee4` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00b5cee8"></a> `00b5cee8` | `bf 42 13 39` | strb wzr,[x21, #0x4d0] | `FALL_THROUGH`
<a id="insn-00b5ceec"></a> `00b5ceec` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b5cef0"></a> `00b5cef0` | `7c 04 02 94` | bl 0x00bde0e0 | `UNCONDITIONAL_CALL`
<a id="insn-00b5cef4"></a> `00b5cef4` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00b5cef8"></a> `00b5cef8` | `81 66 42 f9` | ldr x1,[x20, #0x4c8] | `FALL_THROUGH`
<a id="insn-00b5cefc"></a> `00b5cefc` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b5cf00"></a> `00b5cf00` | `08 59 40 f9` | ldr x8,[x8, #0xb0] | `FALL_THROUGH`
<a id="insn-00b5cf04"></a> `00b5cf04` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00b5cf08"></a> `00b5cf08` | `9f 66 02 f9` | str xzr,[x20, #0x4c8] | `FALL_THROUGH`
<a id="insn-00b5cf0c"></a> `00b5cf0c` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b5cf10"></a> `00b5cf10` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b5cf14"></a> `00b5cf14` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00b5cf18"></a> `00b5cf18` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00b5ceac`](#insn-00b5ceac) 範囲 `[['00b5ceac', '00b5cec7']]`
  - `CONDITIONAL_JUMP` [`00b5cec4`](#insn-00b5cec4) → [`00b5cf0c`](#insn-00b5cf0c)
  - `FALL_THROUGH` [`00b5cec4`](#insn-00b5cec4) → [`00b5cec8`](#insn-00b5cec8)
- ブロック [`00b5cec8`](#insn-00b5cec8) 範囲 `[['00b5cec8', '00b5ced7']]`
  - `CONDITIONAL_JUMP` [`00b5ced4`](#insn-00b5ced4) → [`00b5ceec`](#insn-00b5ceec)
  - `FALL_THROUGH` [`00b5ced4`](#insn-00b5ced4) → [`00b5ced8`](#insn-00b5ced8)
- ブロック [`00b5ced8`](#insn-00b5ced8) 範囲 `[['00b5ced8', '00b5ceeb']]`
  - `FALL_THROUGH` [`00b5cee8`](#insn-00b5cee8) → [`00b5ceec`](#insn-00b5ceec)
- ブロック [`00b5ceec`](#insn-00b5ceec) 範囲 `[['00b5ceec', '00b5cf0b']]`
  - `FALL_THROUGH` [`00b5cf08`](#insn-00b5cf08) → [`00b5cf0c`](#insn-00b5cf0c)
- ブロック [`00b5cf0c`](#insn-00b5cf0c) 範囲 `[['00b5cf0c', '00b5cf1b']]`

## 命令位置別の参照

- [`00b5ceac`](#insn-00b5ceac) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5ceb0`](#insn-00b5ceb0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5ceb4`](#insn-00b5ceb4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5cec0`](#insn-00b5cec0) → `010a14c8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00b5cec4`](#insn-00b5cec4) → [`00b5cf0c`](#insn-00b5cf0c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5cecc`](#insn-00b5cecc) → `010a14d0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00b5ced4`](#insn-00b5ced4) → [`00b5ceec`](#insn-00b5ceec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5cee8`](#insn-00b5cee8) → `010a14d0`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00b5cef0`](#insn-00b5cef0) → [`00bde0e0`](../00bde/00bde0e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde0e0` · 推定シンボル `None` · 推定型 `None`
- [`00b5cef8`](#insn-00b5cef8) → `010a14c8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00b5cf08`](#insn-00b5cf08) → `010a14c8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00b5cf0c`](#insn-00b5cf0c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5cf10`](#insn-00b5cf10) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b5ceac`](#insn-00b5ceac)

~~~json
{
  "source": "00b5ceac",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5ceb0`](#insn-00b5ceb0)

~~~json
{
  "source": "00b5ceb0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5ceb4`](#insn-00b5ceb4)

~~~json
{
  "source": "00b5ceb4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5cec0`](#insn-00b5cec0)

~~~json
{
  "source": "00b5cec0",
  "target": "010a14c8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a14c8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b5cec4`](#insn-00b5cec4)

~~~json
{
  "source": "00b5cec4",
  "target": "00b5cf0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5cecc`](#insn-00b5cecc)

~~~json
{
  "source": "00b5cecc",
  "target": "010a14d0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a14d0",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b5ced4`](#insn-00b5ced4)

~~~json
{
  "source": "00b5ced4",
  "target": "00b5ceec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5cee8`](#insn-00b5cee8)

~~~json
{
  "source": "00b5cee8",
  "target": "010a14d0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a14d0",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b5cef0`](#insn-00b5cef0)

~~~json
{
  "source": "00b5cef0",
  "target": "00bde0e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b5cef8`](#insn-00b5cef8)

~~~json
{
  "source": "00b5cef8",
  "target": "010a14c8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a14c8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b5cf08`](#insn-00b5cf08)

~~~json
{
  "source": "00b5cf08",
  "target": "010a14c8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a14c8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b5cf0c`](#insn-00b5cf0c)

~~~json
{
  "source": "00b5cf0c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5cf10`](#insn-00b5cf10)

~~~json
{
  "source": "00b5cf10",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
