# 00bdaeb8

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b6b9b8`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6b/00b6b9b8.md) · 移動量 `+0x6f500`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/inspection-0019.md#compare-9988d11624f6ef893d963f9f36c09bf2)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bdb2e0`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdb/00bdb2e0.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/inspection-0039.md#compare-b279b91d77c930ab5ce6c51566a31f4f)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdaeb8",
  "name": "_ZN8firebase4auth20JniAuthPhoneListener26nativeOnVerificationFailedEP7_JNIEnvP8_jobjectlP8_jstring",
  "size": 116,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d93ab2474287cb61559bc44b426d49ccdf348845488bd7852e51c18d33a477a8",
  "source_text_sha256": "d93ab2474287cb61559bc44b426d49ccdf348845488bd7852e51c18d33a477a8",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdaeb8",
        "00bdaf2b"
      ]
    ],
    "bytes_sha256": "8475aa8350cbb5d7d6d4d701847683606b4594495977407022b896d7c95d6073",
    "instruction_count": 29,
    "instruction_bytes": 116,
    "body_bytes": 116,
    "indirect": 1,
    "unresolved": 1
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c57ab0](../00c57/00c57ab0.md)
- [00c57ae0](../00c57/00c57ae0.md)
- [00c5ab20](../00c5a/00c5ab20.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 671 bytes

~~~c

void _ZN8firebase4auth20JniAuthPhoneListener26nativeOnVerificationFailedEP7_JNIEnvP8_jobjectlP8_jstring
               (undefined8 param_1,undefined8 param_2,long *param_3,undefined8 param_4)

{
  long lVar1;
  byte local_40 [16];
  void *local_30;
  long local_28;
  
  lVar1 = tpidr_el0;
  local_28 = *(long *)(lVar1 + 0x28);
  _ZN8firebase4util15JStringToStringEP7_JNIEnvP8_jobject(local_40,param_1,param_4);
  (**(code **)(*param_3 + 0x18))(param_3,local_40);
  if ((local_40[0] & 1) != 0) {
    _ZdlPv(local_30);
  }
  if (*(long *)(lVar1 + 0x28) == local_28) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdaeb8"></a> `00bdaeb8` | `ff 03 01 d1` | sub sp,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00bdaebc"></a> `00bdaebc` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bdaec0"></a> `00bdaec0` | `fd 7b 03 a9` | stp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bdaec4"></a> `00bdaec4` | `fd c3 00 91` | add x29,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00bdaec8"></a> `00bdaec8` | `54 d0 3b d5` | mrs x20,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00bdaecc"></a> `00bdaecc` | `88 16 40 f9` | ldr x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00bdaed0"></a> `00bdaed0` | `e1 03 03 aa` | mov x1,x3 | `FALL_THROUGH`
<a id="insn-00bdaed4"></a> `00bdaed4` | `f3 03 02 aa` | mov x19,x2 | `FALL_THROUGH`
<a id="insn-00bdaed8"></a> `00bdaed8` | `e8 0f 00 f9` | str x8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00bdaedc"></a> `00bdaedc` | `e8 03 00 91` | mov x8,sp | `FALL_THROUGH`
<a id="insn-00bdaee0"></a> `00bdaee0` | `10 ff 01 94` | bl 0x00c5ab20 | `UNCONDITIONAL_CALL`
<a id="insn-00bdaee4"></a> `00bdaee4` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bdaee8"></a> `00bdaee8` | `08 0d 40 f9` | ldr x8,[x8, #0x18] | `FALL_THROUGH`
<a id="insn-00bdaeec"></a> `00bdaeec` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-00bdaef0"></a> `00bdaef0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bdaef4"></a> `00bdaef4` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bdaef8"></a> `00bdaef8` | `e8 03 40 39` | ldrb w8,[sp] | `FALL_THROUGH`
<a id="insn-00bdaefc"></a> `00bdaefc` | `68 00 00 36` | tbz w8,#0x0,0x00bdaf08 | `CONDITIONAL_JUMP`
<a id="insn-00bdaf00"></a> `00bdaf00` | `e0 0b 40 f9` | ldr x0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bdaf04"></a> `00bdaf04` | `eb f2 01 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-00bdaf08"></a> `00bdaf08` | `88 16 40 f9` | ldr x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00bdaf0c"></a> `00bdaf0c` | `e9 0f 40 f9` | ldr x9,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00bdaf10"></a> `00bdaf10` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bdaf14"></a> `00bdaf14` | `a1 00 00 54` | b.ne 0x00bdaf28 | `CONDITIONAL_JUMP`
<a id="insn-00bdaf18"></a> `00bdaf18` | `fd 7b 43 a9` | ldp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bdaf1c"></a> `00bdaf1c` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bdaf20"></a> `00bdaf20` | `ff 03 01 91` | add sp,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00bdaf24"></a> `00bdaf24` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bdaf28"></a> `00bdaf28` | `ee f2 01 94` | bl 0x00c57ae0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdaeb8`](#insn-00bdaeb8) 範囲 `[['00bdaeb8', '00bdaeff']]`
  - `CONDITIONAL_JUMP` [`00bdaefc`](#insn-00bdaefc) → [`00bdaf08`](#insn-00bdaf08)
  - `FALL_THROUGH` [`00bdaefc`](#insn-00bdaefc) → [`00bdaf00`](#insn-00bdaf00)
- ブロック [`00bdaf00`](#insn-00bdaf00) 範囲 `[['00bdaf00', '00bdaf07']]`
  - `FALL_THROUGH` [`00bdaf04`](#insn-00bdaf04) → [`00bdaf08`](#insn-00bdaf08)
- ブロック [`00bdaf08`](#insn-00bdaf08) 範囲 `[['00bdaf08', '00bdaf17']]`
  - `CONDITIONAL_JUMP` [`00bdaf14`](#insn-00bdaf14) → [`00bdaf28`](#insn-00bdaf28)
  - `FALL_THROUGH` [`00bdaf14`](#insn-00bdaf14) → [`00bdaf18`](#insn-00bdaf18)
- ブロック [`00bdaf18`](#insn-00bdaf18) 範囲 `[['00bdaf18', '00bdaf27']]`
- ブロック [`00bdaf28`](#insn-00bdaf28) 範囲 `[['00bdaf28', '00bdaf2b']]`

## 命令位置別の参照

- [`00bdaebc`](#insn-00bdaebc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdaec0`](#insn-00bdaec0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdaed8`](#insn-00bdaed8) → `Stack[-0x28]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdaee0`](#insn-00bdaee0) → [`00c5ab20`](../00c5a/00c5ab20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ab20` · 推定シンボル `None` · 推定型 `None`
- [`00bdaef8`](#insn-00bdaef8) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdaefc`](#insn-00bdaefc) → [`00bdaf08`](#insn-00bdaf08) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdaf00`](#insn-00bdaf00) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdaf04`](#insn-00bdaf04) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`00bdaf0c`](#insn-00bdaf0c) → `Stack[-0x28]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdaf14`](#insn-00bdaf14) → [`00bdaf28`](#insn-00bdaf28) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdaf18`](#insn-00bdaf18) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdaf1c`](#insn-00bdaf1c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdaf28`](#insn-00bdaf28) → [`00c57ae0`](../00c57/00c57ae0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ae0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdaebc`](#insn-00bdaebc)

~~~json
{
  "source": "00bdaebc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdaec0`](#insn-00bdaec0)

~~~json
{
  "source": "00bdaec0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdaed8`](#insn-00bdaed8)

~~~json
{
  "source": "00bdaed8",
  "target": "Stack[-0x28]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdaee0`](#insn-00bdaee0)

~~~json
{
  "source": "00bdaee0",
  "target": "00c5ab20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdaef8`](#insn-00bdaef8)

~~~json
{
  "source": "00bdaef8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdaefc`](#insn-00bdaefc)

~~~json
{
  "source": "00bdaefc",
  "target": "00bdaf08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdaf00`](#insn-00bdaf00)

~~~json
{
  "source": "00bdaf00",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdaf04`](#insn-00bdaf04)

~~~json
{
  "source": "00bdaf04",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdaf0c`](#insn-00bdaf0c)

~~~json
{
  "source": "00bdaf0c",
  "target": "Stack[-0x28]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdaf14`](#insn-00bdaf14)

~~~json
{
  "source": "00bdaf14",
  "target": "00bdaf28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdaf18`](#insn-00bdaf18)

~~~json
{
  "source": "00bdaf18",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdaf1c`](#insn-00bdaf1c)

~~~json
{
  "source": "00bdaf1c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdaf28`](#insn-00bdaf28)

~~~json
{
  "source": "00bdaf28",
  "target": "00c57ae0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
