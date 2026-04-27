module encoder_4to2 (
    input D0, D1, D2, D3,
    output Y1, Y0
);

    assign Y1 = D2 | D3;
    assign Y0 = D1 | D3;

endmodule
