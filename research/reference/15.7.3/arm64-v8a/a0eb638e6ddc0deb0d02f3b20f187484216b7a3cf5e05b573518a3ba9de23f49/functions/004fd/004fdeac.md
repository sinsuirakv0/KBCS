# 004fdeac

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `004fdeac`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004fd/004fdeac.md) · 移動量 `+0x0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0012.md#compare-dc4c16c3b385f6ae7cc9894b73866fc7)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `004fdeac`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004fd/004fdeac.md) · 移動量 `+0x0`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0012.md#compare-736f05f663b81279dbb9d2c86f7f8279)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "004fdeac",
  "name": "_ZN5Botan16X509_CertificateC1ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE",
  "size": 216,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "bcb0fdd8e3a84af1ccfd56030dd8b3e3f71965ca55df3eb59045d8b13ceac510",
  "source_text_sha256": "bcb0fdd8e3a84af1ccfd56030dd8b3e3f71965ca55df3eb59045d8b13ceac510",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "004fdeac",
        "004fdf7f"
      ],
      [
        "004fdfd4",
        "004fdfd7"
      ]
    ],
    "bytes_sha256": "745b48c471501686ff5e7ec739bf178732c379b6169d4a0f055d6512cfdc4783",
    "instruction_count": 54,
    "instruction_bytes": 216,
    "body_bytes": 216,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00bdcbc0](../00bdc/00bdcbc0.md)

## 呼び出し先

- [00bdb010](../00bdb/00bdb010.md)
- [00bdb040](../00bdb/00bdb040.md)
- [00bdb7f0](../00bdb/00bdb7f0.md)
- [00bdc7c0](../00bdc/00bdc7c0.md)
- [00bdc7d0](../00bdc/00bdc7d0.md)
- [00bdcde0](../00bdc/00bdcde0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1386 bytes

~~~c

void _ZN5Botan16X509_CertificateC1ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE
               (long *param_1,undefined8 param_2)

{
  undefined *puVar1;
  long lVar2;
  ushort local_70 [8];
  void *local_60;
  long local_38;
  
  lVar2 = tpidr_el0;
  local_38 = *(long *)(lVar2 + 0x28);
  puVar1 = PTR__ZTVN5Botan19AlgorithmIdentifierE_00c1aef8 + 0x10;
  *param_1 = (long)(PTR__ZTVN5Botan11X509_ObjectE_00c1b318 + 0x10);
  param_1[1] = (long)puVar1;
  local_70[0] = 0;
  _ZN5Botan3OIDC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE
            (param_1 + 2,local_70);
  if ((local_70[0] & 1) != 0) {
    _ZdlPv(local_60);
  }
  param_1[0xe] = 0;
  param_1[0xb] = 0;
  param_1[10] = 0;
  param_1[0xd] = 0;
  param_1[0xc] = 0;
  puVar1 = PTR__ZTVN5Botan16X509_CertificateE_00c1b2a0;
  param_1[7] = 0;
  param_1[6] = 0;
  param_1[9] = 0;
  param_1[8] = 0;
  param_1[0xf] = 0;
  param_1[0x10] = 0;
  *param_1 = (long)(puVar1 + 0x10);
  _ZN5Botan17DataSource_StreamC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEb
            (local_70,param_2,1);
  _ZN5Botan11X509_Object9load_dataERNS_10DataSourceE(param_1,local_70);
  _ZN5Botan17DataSource_StreamD2Ev(local_70);
  if (*(long *)(lVar2 + 0x28) == local_38) {
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
<a id="insn-004fdeac"></a> `004fdeac` | `ff c3 01 d1` | sub sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-004fdeb0"></a> `004fdeb0` | `fd 7b 04 a9` | stp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-004fdeb4"></a> `004fdeb4` | `f6 57 05 a9` | stp x22,x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-004fdeb8"></a> `004fdeb8` | `f4 4f 06 a9` | stp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-004fdebc"></a> `004fdebc` | `fd 03 01 91` | add x29,sp,#0x40 | `FALL_THROUGH`
<a id="insn-004fdec0"></a> `004fdec0` | `56 d0 3b d5` | mrs x22,tpidr_el0 | `FALL_THROUGH`
<a id="insn-004fdec4"></a> `004fdec4` | `e8 38 00 d0` | adrp x8,0xc1b000 | `FALL_THROUGH`
<a id="insn-004fdec8"></a> `004fdec8` | `ea 38 00 b0` | adrp x10,0xc1a000 | `FALL_THROUGH`
<a id="insn-004fdecc"></a> `004fdecc` | `08 8d 41 f9` | ldr x8,[x8, #0x318] | `FALL_THROUGH`
<a id="insn-004fded0"></a> `004fded0` | `c9 16 40 f9` | ldr x9,[x22, #0x28] | `FALL_THROUGH`
<a id="insn-004fded4"></a> `004fded4` | `4a 7d 47 f9` | ldr x10,[x10, #0xef8] | `FALL_THROUGH`
<a id="insn-004fded8"></a> `004fded8` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-004fdedc"></a> `004fdedc` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-004fdee0"></a> `004fdee0` | `08 41 00 91` | add x8,x8,#0x10 | `FALL_THROUGH`
<a id="insn-004fdee4"></a> `004fdee4` | `a9 83 1f f8` | stur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-004fdee8"></a> `004fdee8` | `49 41 00 91` | add x9,x10,#0x10 | `FALL_THROUGH`
<a id="insn-004fdeec"></a> `004fdeec` | `08 24 81 a8` | stp x8,x9,[x0], #0x10 | `FALL_THROUGH`
<a id="insn-004fdef0"></a> `004fdef0` | `ff 03 00 79` | strh wzr,[sp] | `FALL_THROUGH`
<a id="insn-004fdef4"></a> `004fdef4` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-004fdef8"></a> `004fdef8` | `3e 76 1b 94` | bl 0x00bdb7f0 | `UNCONDITIONAL_CALL`
<a id="insn-004fdefc"></a> `004fdefc` | `e8 03 40 39` | ldrb w8,[sp] | `FALL_THROUGH`
<a id="insn-004fdf00"></a> `004fdf00` | `68 00 00 36` | tbz w8,#0x0,0x004fdf0c | `CONDITIONAL_JUMP`
<a id="insn-004fdf04"></a> `004fdf04` | `e0 0b 40 f9` | ldr x0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-004fdf08"></a> `004fdf08` | `42 74 1b 94` | bl 0x00bdb010 | `UNCONDITIONAL_CALL`
<a id="insn-004fdf0c"></a> `004fdf0c` | `00 e4 00 6f` | movi v0.2D,#0x0 | `FALL_THROUGH`
<a id="insn-004fdf10"></a> `004fdf10` | `7f 3a 00 f9` | str xzr,[x19, #0x70] | `FALL_THROUGH`
<a id="insn-004fdf14"></a> `004fdf14` | `e8 38 00 d0` | adrp x8,0xc1b000 | `FALL_THROUGH`
<a id="insn-004fdf18"></a> `004fdf18` | `f5 03 13 aa` | mov x21,x19 | `FALL_THROUGH`
<a id="insn-004fdf1c"></a> `004fdf1c` | `60 82 02 ad` | stp q0,q0,[x19, #0x50] | `FALL_THROUGH`
<a id="insn-004fdf20"></a> `004fdf20` | `08 51 41 f9` | ldr x8,[x8, #0x2a0] | `FALL_THROUGH`
<a id="insn-004fdf24"></a> `004fdf24` | `60 82 01 ad` | stp q0,q0,[x19, #0x30] | `FALL_THROUGH`
<a id="insn-004fdf28"></a> `004fdf28` | `bf 8e 07 f8` | str xzr,[x21, #0x78]! | `FALL_THROUGH`
<a id="insn-004fdf2c"></a> `004fdf2c` | `08 41 00 91` | add x8,x8,#0x10 | `FALL_THROUGH`
<a id="insn-004fdf30"></a> `004fdf30` | `7f 42 00 f9` | str xzr,[x19, #0x80] | `FALL_THROUGH`
<a id="insn-004fdf34"></a> `004fdf34` | `68 02 00 f9` | str x8,[x19] | `FALL_THROUGH`
<a id="insn-004fdf38"></a> `004fdf38` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-004fdf3c"></a> `004fdf3c` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-004fdf40"></a> `004fdf40` | `22 00 80 52` | mov w2,#0x1 | `FALL_THROUGH`
<a id="insn-004fdf44"></a> `004fdf44` | `1f 7a 1b 94` | bl 0x00bdc7c0 | `UNCONDITIONAL_CALL`
<a id="insn-004fdf48"></a> `004fdf48` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-004fdf4c"></a> `004fdf4c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-004fdf50"></a> `004fdf50` | `a4 7b 1b 94` | bl 0x00bdcde0 | `UNCONDITIONAL_CALL`
<a id="insn-004fdf54"></a> `004fdf54` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-004fdf58"></a> `004fdf58` | `1e 7a 1b 94` | bl 0x00bdc7d0 | `UNCONDITIONAL_CALL`
<a id="insn-004fdf5c"></a> `004fdf5c` | `c8 16 40 f9` | ldr x8,[x22, #0x28] | `FALL_THROUGH`
<a id="insn-004fdf60"></a> `004fdf60` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-004fdf64"></a> `004fdf64` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-004fdf68"></a> `004fdf68` | `61 03 00 54` | b.ne 0x004fdfd4 | `CONDITIONAL_JUMP`
<a id="insn-004fdf6c"></a> `004fdf6c` | `f4 4f 46 a9` | ldp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-004fdf70"></a> `004fdf70` | `f6 57 45 a9` | ldp x22,x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-004fdf74"></a> `004fdf74` | `fd 7b 44 a9` | ldp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-004fdf78"></a> `004fdf78` | `ff c3 01 91` | add sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-004fdf7c"></a> `004fdf7c` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-004fdfd4"></a> `004fdfd4` | `1b 74 1b 94` | bl 0x00bdb040 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`004fdeac`](#insn-004fdeac) 範囲 `[['004fdeac', '004fdf03']]`
  - `CONDITIONAL_JUMP` [`004fdf00`](#insn-004fdf00) → [`004fdf0c`](#insn-004fdf0c)
  - `FALL_THROUGH` [`004fdf00`](#insn-004fdf00) → [`004fdf04`](#insn-004fdf04)
- ブロック [`004fdf04`](#insn-004fdf04) 範囲 `[['004fdf04', '004fdf0b']]`
  - `FALL_THROUGH` [`004fdf08`](#insn-004fdf08) → [`004fdf0c`](#insn-004fdf0c)
- ブロック [`004fdf0c`](#insn-004fdf0c) 範囲 `[['004fdf0c', '004fdf6b']]`
  - `CONDITIONAL_JUMP` [`004fdf68`](#insn-004fdf68) → [`004fdfd4`](#insn-004fdfd4)
  - `FALL_THROUGH` [`004fdf68`](#insn-004fdf68) → [`004fdf6c`](#insn-004fdf6c)
- ブロック [`004fdf6c`](#insn-004fdf6c) 範囲 `[['004fdf6c', '004fdf7f']]`
- ブロック [`004fdfd4`](#insn-004fdfd4) 範囲 `[['004fdfd4', '004fdfd7']]`

## 命令位置別の参照

- [`004fdeb0`](#insn-004fdeb0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fdeb4`](#insn-004fdeb4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fdeb8`](#insn-004fdeb8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fdecc`](#insn-004fdecc) → `00c1b318`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`004fded4`](#insn-004fded4) → `00c1aef8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`004fdee4`](#insn-004fdee4) → `Stack[-0x38]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fdeec`](#insn-004fdeec) → `00beca10`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1[72]`
- [`004fdeec`](#insn-004fdeec) → `00be9198`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1[48]`
- [`004fdef0`](#insn-004fdef0) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fdef8`](#insn-004fdef8) → [`00bdb7f0`](../00bdb/00bdb7f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb7f0` · 推定シンボル `None` · 推定型 `None`
- [`004fdefc`](#insn-004fdefc) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fdf00`](#insn-004fdf00) → [`004fdf0c`](#insn-004fdf0c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fdf04`](#insn-004fdf04) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fdf08`](#insn-004fdf08) → [`00bdb010`](../00bdb/00bdb010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb010` · 推定シンボル `None` · 推定型 `None`
- [`004fdf20`](#insn-004fdf20) → `00c1b2a0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`004fdf34`](#insn-004fdf34) → `00beaa78`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1[72]`
- [`004fdf44`](#insn-004fdf44) → [`00bdc7c0`](../00bdc/00bdc7c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdc7c0` · 推定シンボル `None` · 推定型 `None`
- [`004fdf50`](#insn-004fdf50) → [`00bdcde0`](../00bdc/00bdcde0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdcde0` · 推定シンボル `None` · 推定型 `None`
- [`004fdf58`](#insn-004fdf58) → [`00bdc7d0`](../00bdc/00bdc7d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdc7d0` · 推定シンボル `None` · 推定型 `None`
- [`004fdf60`](#insn-004fdf60) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fdf68`](#insn-004fdf68) → [`004fdfd4`](#insn-004fdfd4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fdf6c`](#insn-004fdf6c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fdf70`](#insn-004fdf70) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fdf74`](#insn-004fdf74) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fdfd4`](#insn-004fdfd4) → [`00bdb040`](../00bdb/00bdb040.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb040` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`004fdeb0`](#insn-004fdeb0)

~~~json
{
  "source": "004fdeb0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fdeb4`](#insn-004fdeb4)

~~~json
{
  "source": "004fdeb4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fdeb8`](#insn-004fdeb8)

~~~json
{
  "source": "004fdeb8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fdecc`](#insn-004fdecc)

~~~json
{
  "source": "004fdecc",
  "target": "00c1b318",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1b318",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`004fded4`](#insn-004fded4)

~~~json
{
  "source": "004fded4",
  "target": "00c1aef8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1aef8",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`004fdee4`](#insn-004fdee4)

~~~json
{
  "source": "004fdee4",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fdeec`](#insn-004fdeec)

~~~json
{
  "source": "004fdeec",
  "target": "00beca10",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00beca00",
  "offset": 16,
  "size": 72,
  "datatype": "undefined1[72]",
  "capture_state": "contains_relocation"
}
~~~
- 参照命令 [`004fdeec`](#insn-004fdeec)

~~~json
{
  "source": "004fdeec",
  "target": "00be9198",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00be9188",
  "offset": 16,
  "size": 48,
  "datatype": "undefined1[48]",
  "capture_state": "contains_relocation"
}
~~~
- 参照命令 [`004fdef0`](#insn-004fdef0)

~~~json
{
  "source": "004fdef0",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fdef8`](#insn-004fdef8)

~~~json
{
  "source": "004fdef8",
  "target": "00bdb7f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004fdefc`](#insn-004fdefc)

~~~json
{
  "source": "004fdefc",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fdf00`](#insn-004fdf00)

~~~json
{
  "source": "004fdf00",
  "target": "004fdf0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fdf04`](#insn-004fdf04)

~~~json
{
  "source": "004fdf04",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fdf08`](#insn-004fdf08)

~~~json
{
  "source": "004fdf08",
  "target": "00bdb010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004fdf20`](#insn-004fdf20)

~~~json
{
  "source": "004fdf20",
  "target": "00c1b2a0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1b2a0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`004fdf34`](#insn-004fdf34)

~~~json
{
  "source": "004fdf34",
  "target": "00beaa78",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00beaa68",
  "offset": 16,
  "size": 72,
  "datatype": "undefined1[72]",
  "capture_state": "contains_relocation"
}
~~~
- 参照命令 [`004fdf44`](#insn-004fdf44)

~~~json
{
  "source": "004fdf44",
  "target": "00bdc7c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004fdf50`](#insn-004fdf50)

~~~json
{
  "source": "004fdf50",
  "target": "00bdcde0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004fdf58`](#insn-004fdf58)

~~~json
{
  "source": "004fdf58",
  "target": "00bdc7d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004fdf60`](#insn-004fdf60)

~~~json
{
  "source": "004fdf60",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fdf68`](#insn-004fdf68)

~~~json
{
  "source": "004fdf68",
  "target": "004fdfd4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fdf6c`](#insn-004fdf6c)

~~~json
{
  "source": "004fdf6c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fdf70`](#insn-004fdf70)

~~~json
{
  "source": "004fdf70",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fdf74`](#insn-004fdf74)

~~~json
{
  "source": "004fdf74",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fdfd4`](#insn-004fdfd4)

~~~json
{
  "source": "004fdfd4",
  "target": "00bdb040",
  "target_space": "ram",
  "resolution": "function"
}
~~~
